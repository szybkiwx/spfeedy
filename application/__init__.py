from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
#from models import User

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+ os.path.join(basedir, 'db', 'spfeedy.db')

app.secret_key = "T<m\xe6p\xea\xff\\\x8bJa\xf8aD\x1fb"
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from application import models, views

@login_manager.user_loader
def load_user(userid):
    from models import User
    return db.session.query(User).filter(User.id == userid).first()


