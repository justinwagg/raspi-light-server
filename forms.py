from flask_wtf import FlaskForm
import datetime
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms_components import TimeField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('button')


class TestForm(FlaskForm):		   
    field1 = SelectField('Device', choices=[('1', 'Device 1'), ('2', 'Device 2')], validators=[DataRequired()])
    field2 = TimeField('On Time', default=datetime.datetime.now().time(), validators=[DataRequired()])
    field3 = TimeField('Off Time', default=datetime.datetime.now().time(), validators=[DataRequired()])
    field4 = IntegerField('Low Light Setting', default = 30, validators=[DataRequired()])
    field5 = IntegerField('High Light Setting', default = 200, validators=[DataRequired()])
    field6 = IntegerField('Manual Light Setting', default = 255, validators=[DataRequired()])
    submit = SubmitField('button')
