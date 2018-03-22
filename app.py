from flask import Flask, render_template, request, flash, redirect, url_for
from config import Config
from forms import LoginForm, SettingsForm
import sqlite3 as sql
import datetime
from flask_bootstrap import Bootstrap
from pytz import timezone
import mysql.connector
import paho.mqtt.client as mqtt
import pprint as p
import json
from singledispatch import singledispatch

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

CLIENT_NAME = "auto_script"
BROKER_ADRESS = "localhost"
client = mqtt.Client(CLIENT_NAME)
client.connect(BROKER_ADRESS, keepalive=10)
client.loop_start()

con = mysql.connector.connect(passwd=Config.MYSQL_PASS, db="flaskapp", host="localhost", user=Config.MYSQL_USER)
con.row_factory = sql.Row
d_cur = con.cursor(dictionary=True)
cur = con.cursor()

d_cur.execute('select * from flaskapp.device_map')
device_map = d_cur.fetchall()

@singledispatch
def to_serializable(val):
    """Used by default."""
    return str(val)

def light_map(x):
    return [device for device in device_map if device['device_id'] == x][0]['device_topic']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/light-settings', methods=['GET', 'POST'])
def settings():
    form = SettingsForm()

    if form.validate_on_submit():
        device_choices = form.device.data
        try:
            for device in device_choices:
                x = form.data
                x['device'] = int(device)

                # Record new data in MySQL
                cur.execute("insert into flaskapp.device_settings (device_id, on_time, low_time, off_time, low, high, manual, created_on) values (%s,%s,%s,%s,%s,%s,%s,%s)", (device, request.form['on_time'], request.form['low_time'], request.form['off_time'], request.form['low'], request.form['high'], request.form['manual'], datetime.datetime.now(timezone('EST'))))
                con.commit()
                print('SQL Insert Success')

                # Publish to MQTT Subscribers
                client.publish(light_map(int(device)), json.dumps(x,  default=to_serializable), qos=1)
                client.publish('all_devices_monitor', json.dumps(x,  default=to_serializable), qos=1)

        except sql.Error as er:
            con.rollback()
            print("An error occurred: %".format(e.args[0]))
    elif form.validate_on_submit() == False:
        print(form.errors)
        pass
    if request.method == 'POST':
        return redirect(url_for('testform'))
    else:
        # Go get the settings
        cur.execute("select c.device_name, time_format(a.on_time, '%h:%i %p'), time_format(a.low_time, '%h:%i %p'), time_format(a.off_time, '%h:%i %p'), a.low, a.high, a.manual, a.created_on from flaskapp.device_settings a inner join (select device_id, max(id) as id from flaskapp.device_settings group by 1 ) b on a.device_id=b.device_id and a.id = b.id left join flaskapp.device_map c on a.device_id = c.device_id")
        row = cur.fetchall()
        return render_template('settings.html', form=form, rows=row, title='Light Control')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
