from flask_wtf import FlaskForm

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
    field2 = SelectField('Mode', choices=[('1', 'Mode 1'), ('2', 'Mode 2')], validators=[DataRequired()])
    field3 = TimeField('On Time', validators=[DataRequired()])
    field4 = TimeField('Off Time', validators=[DataRequired()])
    field5 = IntegerField('Light Value', validators=[DataRequired()])
    submit = SubmitField('button')
