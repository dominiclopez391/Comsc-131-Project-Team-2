from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))
myobj = Flask(__name__) #referenced and run in run.py

myobj.config.from_mapping(
        SECRET_KEY = 'mypassword',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "appdb"),
        SQLALCHEMY_TRACK_MODIFICATIONS = False,

)

db = SQLAlchemy(myobj)

login = LoginManager(myobj)
login.login_view = 'login'

from myapp import routes
