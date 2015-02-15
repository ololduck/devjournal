from . import db
from markdown import markdown
from datetime import datetime as dt


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    md = db.Column(db.Text)
    last_modified = db.Column(db.DateTime)
    html = db.Column(db.Text)

    def save(self):
        self.html = markdown(self.md)
        self.last_modified = dt.now()
        db.session.add(self)
        db.session.commit()
