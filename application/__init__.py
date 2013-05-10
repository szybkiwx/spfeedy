from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+ os.path.join(basedir, 'db', 'spfeedy.db')
db = SQLAlchemy(app)

from application import models, views
