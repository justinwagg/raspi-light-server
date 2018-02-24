from flask import Flask, render_template, request, flash, redirect
from config import Config
from forms import LoginForm, TestForm
import sqlite3 as sql


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/testform', methods=['GET', 'POST'])
def testform():
    form = TestForm()
    if form.validate_on_submit():
        print(request.form['field1'])
        print(request.form['field2'])
        print(request.form['field3'])
        print(request.form['field4'])
        print(request.form['field5'])   
        try:
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO test_table2 (device, mode, on_time, off_time, light_value) VALUES (?,?,?,?,?)", (request.form['field1'], request.form['field2'], request.form['field3'], request.form['field4'], request.form['field5']))
                con.commit()
                print('SQL Insert Success')
        except sql.Error as er:
            con.rollback()
            # print('SQL Insert Error: {}'.format(er.message))
            print("An error occurred: %".format(e.args[0]))
    else:
        print('Form Validity Error')
        print(form.errors)
    return render_template('testform.html', form=form)





@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    msg = 'tetst'
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            print(nm)
            addr = request.form['add']
            print(addr)
            city = request.form['city']
            print(city)
            pin = request.form['pin']
            print(pin)         
            with sql.connect("database.db") as con:
                cur = con.cursor()
                # cur.execute("insert into students (name,addr,city,pin) values ('Emma', '21-39 24th St', 'Astoria', '1111')")
                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"  
        finally:
            return render_template("result.html",msg = msg)
            con.close()

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from students")
    
    rows = cur.fetchall(); 
    return render_template("list.html",rows = rows)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
