from flask_wtf import FlaskForm
import datetime
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, SelectMultipleField, widgets
from wtforms_components import TimeField
from wtforms.validators import DataRequired, NumberRange

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('button')


class SettingsForm(FlaskForm):		   
    # field1 = SelectField('Device', choices=[('1', 'Bathroom'), ('2', 'Steps')], validators=[DataRequired()])
    device = SelectMultipleField('Light', choices=[('1', 'Bathroom'), ('2', 'Steps'), ('3', 'Kitchen')], option_widget=widgets.CheckboxInput(), widget=widgets.ListWidget(prefix_label=False))
    on_time = TimeField('On Time', default=datetime.time(17, 0))
    low_time = TimeField('Low Time', default=datetime.time(23, 30))
    off_time = TimeField('Off Time', default=datetime.time(7, 30))
    low = IntegerField('Low Light Setting (0-100)', default = 30, validators=[DataRequired(), NumberRange(min=0, max=100, message='Values from 0-100')])
    high = IntegerField('High Light Setting (0-100)', default = 75, validators=[DataRequired(), NumberRange(min=0, max=100, message='Values from 0-100')])
    manual = IntegerField('Manual Light Setting (0-100)', default = 100, validators=[DataRequired(), NumberRange(min=0, max=100, message='Values from 0-100')])
    submit = SubmitField('Submit')
