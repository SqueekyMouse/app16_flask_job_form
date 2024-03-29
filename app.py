from datetime import datetime
from flask import Flask,render_template, request, flash
from flask_sqlalchemy import SQLAlchemy #sql/sqlite but interacts with flask!!!
from flask_mail import Mail, Message #mail from flask!!

app=Flask(__name__)

app.config['SECRET_KEY']='myapplication123'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db' #db path!!
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USE_SSL']=True
app.config['MAIL_USERNAME']='appuser565@gmail.com'
app.config['MAIL_PASSWORD']='tymmrvjrnawimuqu'

db=SQLAlchemy(app)

mail=Mail(app) #connect mail to our app!!

# create a db model!!!
class Form(db.Model): #class name can be any!!
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(80))
    last_name=db.Column(db.String(80))
    email=db.Column(db.String(80))
    date=db.Column(db.Date)
    occupation=db.Column(db.String(80))

@app.route("/", methods=['GET','POST']) #url to handle get and post reqs!!!
def index():
    # print(request.method)
    if request.method=='POST': #for submit button!!!
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        email=request.form['email']
        date=request.form['date']
        date_obj=datetime.strptime(date,'%Y-%m-%d') #db needs date obj!!
        occupation=request.form['occupation']
        
        form=Form(first_name=first_name, last_name=last_name,
                  email=email, date=date_obj, occupation=occupation)
        db.session.add(form)
        db.session.commit()

        message_body=f'Thank you for your submission, {first_name}. '\
        f'Here are your data:\n{first_name}\n{last_name}\n{date}\n'\
        f'Thank you'
        message=Message(subject='New form submission', 
                        sender=app.config['MAIL_USERNAME'],
                        recipients=[email],
                        body=message_body)
        mail.send(message)

        flash(f'{first_name}, your form was submitted successfully!', 'success')

    return(render_template("index.html"))


if __name__=='__main__':
    with app.app_context():
        db.create_all() #this will create the db file if it doesnt exist!!!
        app.run(debug=True,port=5001)

