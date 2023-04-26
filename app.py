from flask import Flask,redirect,url_for,render_template,request
import os
from form import *

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

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/form')
def form():
    form=BookingForm()
    # check request method
    if request.method=='POST':
        if form.validate_on_submit:
            print(form.email.data)
        return redirect(url_for('index'))
    # check form validation
    # check errors
    return render_template('form.html', form=form)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)