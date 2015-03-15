from os import environ
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

__version__ = '0.0.1'

app = Flask('devjournal')
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL', 'sqlite:////tmp/testdb') #noqa
app.config['DEBUG'] = True
manager = Manager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

md_exts = [
    'markdown.extensions.extra',
    'markdown.extensions.admonition',
    'markdown.extensions.codehilite',
]

from . import views, models, utils # noqa
