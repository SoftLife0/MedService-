from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField, RadioField, DateField, FileField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from wtforms.widgets import TextArea

class BookingForm(FlaskForm):
    visit = SelectField('Have You Visited Us Before?', choices=[("-Select-","-Select-"),("New Patient","New Patient"),("Returning Patient","Returning Patient"),("Other","Other")])
    doctor = SelectField('Select Doctor', choices=[("-Select Doctor-","-Select Doctor-"),("Jonathan Barnes D.M.","Jonathan Barnes D.M."),("Hannah Harper D.M.","Hannah Harper D.M."),("Megan Coleman D.M.","Megan Coleman D.M."),("Matthew Anderson D.M.","Matthew Anderson D.M."),("Robert Peterson D.M.","Robert Peterson D.M."),("Joshua Elledge D.M.","Joshua Elledge D.M.")])
    date = DateField('Set Appointment Date', format='%Y-%m-%d' )
    name = StringField('Enter Full Name', validators=[DataRequired()])
    email = StringField('Enter Your E-mail', validators=[DataRequired()])
    contact = IntegerField('Enter Your Phone Number', validators=[DataRequired()])
    # text = StringField('Your Message', widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField('Next')
