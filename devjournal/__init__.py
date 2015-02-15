from os import environ
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask('devjournal')
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL', 'sqlite:////tmp/testdb') #noqa
app.config['DEBUG'] = True
db = SQLAlchemy(app)
db.create_all()


from . import views, models # noqa
