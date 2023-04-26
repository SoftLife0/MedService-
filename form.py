from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField, RadioField, DateField, FileField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

class BookingForm(FlaskForm):
    nameofclient = StringField('Enter Full Name', validators=[DataRequired()])
    contact = IntegerField('Enter Contact Number', validators=[DataRequired()])
    email = StringField('Enter valid E-mail', validators=[DataRequired()])
    room = SelectField('Choice of Package', choices=[("-Select-","-Select-"),("-Select-","-Select-")])
    arrivaldate = DateField('Date of Arrival', format='%Y-%m-%d' )
    submit = SubmitField('Next')
