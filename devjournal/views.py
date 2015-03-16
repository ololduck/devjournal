# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import render_template, abort, redirect, request, jsonify
from . import app
from .models import Page, ProjectPage, EventPage
from .utils import get_page_and_type, render_project_page, render_event_page
from .utils import cat_create_if_not_exist


@app.route('/')
def index():
    return '<h1>Nothing to see here</h1><p>(For now)</p>'


@app.route('/<string:page_name>')
def view(page_name):
    page = ProjectPage.query.filter_by(name=page_name).first()
    if page:
        return render_project_page(page)
    page = EventPage.query.filter_by(name=page_name).first()
    if page:
        return render_event_page(page)
    page = Page.query.filter_by(name=page_name).first()
    if not page:
        abort(404)
    return render_template('page.html', page=page)


@app.route('/<string:page_name>/edit', methods=['GET', 'POST'])
def edit(page_name):
    page, t = get_page_and_type(page_name)
    if not page:
        abort(404)
    if request.method == 'POST':
        if 'page_name' in request.json:
            page.name = request.json.get('page_name')
        if 'page_content' in request.json:
            page.md = request.json.get('page_content')
        if 'page_categories' in request.json:
            page.categories = [cat_create_if_not_exist(cat_name)
                               for cat_name.strip() in request.json.get(
                'page_categories').split(',')]
        page.save()
        if page.name != page_name:
            return jsonify({'redirect': '/{0}/edit'.format(page.name)})
    return render_template('edit.html', page=page, page_type=t.__name__)


@app.route('/<string:page_name>/create', methods=['GET', 'POST'])
def create(page_name):
    if request.method == 'POST':
        if 'page_type' not in request.form or 'page_name' not in request.form:
            abort(400)
        if request.form.get('page_type') == 'event':
            page = EventPage()
        elif request.form.get('page_type') == 'project':
            page = ProjectPage()
        else:
            page = Page()
        page.name = page_name
        page.md = ""
        page.save()
        return redirect('/{0}/edit'.format(page_name))
    page, _ = get_page_and_type(page_name)
    if page:
        return redirect('/{0}/edit'.format(page_name))
    return render_template('create.html', page_name=page_name)
