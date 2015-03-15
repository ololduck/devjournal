from . import db, md_exts
from markdown import markdown
from datetime import datetime as dt
from sqlalchemy.orm import relationship


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    base64 = db.Column(db.Text)

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


cat_page_association_table = db.Table('association', db.Model.metadata,
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id')),
    db.Column('page_id', db.Integer, db.ForeignKey('pages.id'))
)


class Page(db.Model):
    __tablename__ = 'pages'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    md = db.Column(db.Text)
    last_modified = db.Column(db.DateTime)
    html = db.Column(db.Text)
    categories = relationship('Category', secondary=cat_page_association_table)

    def save(self):
        self.html = markdown(self.md, extensions=md_exts)
        self.last_modified = dt.now()
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


class ProjectPage(Page):
    __tablename__ = "projectpages"
    id = db.Column(db.Integer, db.ForeignKey('pages.id'), primary_key=True)
    repo_url = db.Column(db.String(256), unique=True)


class EventPage(Page):
    __tablename__ = "eventpages"
    id = db.Column(db.Integer, db.ForeignKey('pages.id'), primary_key=True)
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    location = db.Column(db.String(256))