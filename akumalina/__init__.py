from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bower import Bower
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
Bower(app)

from akumalina import routes
from akumalina import models
