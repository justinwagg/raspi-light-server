from flask import Flask, render_template, request, flash, redirect
from config import Config
from forms import LoginForm, TestForm
import sqlite3 as sql
import datetime

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/testform', methods=['GET', 'POST'])
def testform():
    form = TestForm()
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from device_settings")
    row = cur.fetchall()
    con.close();
    if form.validate_on_submit(): 
        try:
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO device_settings (device_id, on_time, off_time, low, high, manual, created_on) VALUES (?,?,?,?,?,?,?)", (request.form['field1'], request.form['field2'], request.form['field3'], request.form['field4'], request.form['field5'], request.form['field6'], datetime.datetime.now()))
                con.commit()
                print('SQL Insert Success')
        except sql.Error as er:
            con.rollback()
            # print('SQL Insert Error: {}'.format(er.message))
            print("An error occurred: %".format(e.args[0])) 
    else:
        print('Form Validity Error')
        print(form.errors)
    return render_template('testform.html', form=form, rows=row)


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from students")
    
    rows = cur.fetchall(); 
    print(rows)
    return render_template("list.html", rows=rows)

@app.route('/list2')
def list2():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from test_table2")
    rows = cur.fetchall(); 
    print(rows)
    return render_template("list2.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
