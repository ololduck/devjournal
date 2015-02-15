from flask import render_template, abort
from . import app
from .models import Page


@app.route('/')
def index():
    return '<h1>Nothing to see here</h1><p>(For now)</p>'


@app.route('/<string:page_name>')
def view(page_name):
    page = Page.query.filter_by(name=page_name).first()
    if not page:
        abort(404)
    return render_template('page.html', page=page)
