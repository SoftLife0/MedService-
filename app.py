from flask import Flask,redirect,url_for,render_template,request
import os
from form import *
from email.message import EmailMessage
import smtplib
import requests
import datetime

app=Flask(__name__)


app.config['UPLOAD_FOLDER']='Documents'
app.config['SECRET_KEY'] = '5791628basdfsadfa32242sdfsfde280ab425'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'


@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

@app.route('/doctor')
def doctor():
    return render_template('doctor.html')

@app.route('/profile2')
def profile2():
    return render_template('profile2.html')

@app.route('/profile3')
def profile3():
    return render_template('profile3.html')

@app.route('/profile4')
def profile4():
    return render_template('profile4.html')

@app.route('/profile5')
def profile5():
    return render_template('profile5.html')

@app.route('/profile6')
def profile6():
    return render_template('profile6.html')

@app.route('/success')
def success():
    return render_template('success.html')

def sendMail(recipient, email):
    sender_email = 'pay@prestoghana.com'
    receiver_email  = recipient
    smtp_server = 'mail.privateemail.com'
    port = 465
    login = 'pay@prestoghana.com'
    password = 'Babebabe123$'

    message = EmailMessage()
    message["Subject"] = "Appointment Confirmation"
    message["From"] = f"MedService <{sender_email}>"
    message["To"] = receiver_email
 
    # content = "Hello world"
    msg = email
    message.set_content(msg, subtype='html')

    server = smtplib.SMTP_SSL(smtp_server, port)
    server.login(login, password)
    server.send_message(message)
    server.quit()
    # sendsms('0556034340', msg)
    return "Done!"

@app.route('/form', methods=['GET','POST'])
def patientform():
    form=BookingForm()
    print(request.method)
    # check request method
    if request.method=='POST':
        if form.validate_on_submit():
            print("vali")
            
            print(form.name.data)
            msg = "Dear " + form.name.data + ",\nI hope this email finds you well. This is to confirm your appointment with Dr." + form.doctor.data + " on " + str(form.date.data) + ".\nIf you have any questions or concerns regarding your appointment, please do not hesitate to contact us at info@medservice.com via email.\nWe look forward to seeing you soon!\nSincerely,\n" + form.doctor.data 
            # email = 'onikosiadewale18@gmail.com'
            print(msg)
            try:
                sendMail(form.email.data, msg)
            except Exception as e:
                print(e)
            return redirect(url_for('success'))
        else:
            print(form.errors)
    # check form validation
    # check errors
    return render_template('form.html', form=form)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)