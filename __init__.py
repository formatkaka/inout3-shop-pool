from flask import  Flask

from flask_bootstrap import Bootstrap

from flask_mail import Mail

from flask_restful import Resource, Api

from flask.ext.sqlalchemy import SQLAlchemy

### Flask instatiate ###

app = Flask(__name__, static_folder='static')

### email config ###

app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'collegeconnect'
app.config['MAIL_PASSWORD'] = 'collegeconnect132736'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/mydb'
#
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mcjzbkaskqhhpu:YA55RPOKl6n5VFfAV-ixxIpO1c@ec2-54-243-201-107.compute-1.amazonaws.com:5432/d6lbt3ijelkme0'

app.config['SECRET_KEY'] = 'SUYGI87 TP4Y GT34T'

db = SQLAlchemy(app)
api = Api(app)
mail = Mail(app)
bootstrap = Bootstrap(app)

from app import views, models

