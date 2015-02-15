from flask import Flask

app = Flask('devjournal')

from . import routes # noqa
