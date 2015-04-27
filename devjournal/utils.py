"""
Utilities, stuff i didn't feel like including elsewhere.
"""
from flask import render_template
from .models import ProjectPage, EventPage, Page, Category


def render_page(page):
    if page.__class__ is Page:
        return render_template("edit.html", page=page,
                               page_type=page.__class__.__name__)
    else:
        return render_template("edit_multitab.html", page=page,
                               page_type=page.__class__.__name__)


def get_page_and_type(page_name):
    """
    Returns the page and its underlying class. Why not only return the object,
    and let the user decide if he want its type via page.__class__?
    I don't know. I fear inheritance on this.

    :param page_name: should be a utf-8 encoded string
    :return: The models.Page object, with its class.
    """
    page = ProjectPage.query.filter_by(name=page_name).first()
    if page:
        return page, ProjectPage
    page = EventPage.query.filter_by(name=page_name).first()
    if page:
        return page, EventPage
    page = Page.query.filter_by(name=page_name).first()
    if page:
        return page, Page
    return None, None


def cat_create_if_not_exist(cat_name):
    """
    :param cat_name: The name of the category. The category model is pretty
                     simple.
    :return: A category that has already been saved in DB, and created if it
             didn't exist previously.
    """
    cat = Category.query.filter_by(name=cat_name).first()
    if cat:
        return cat
    cat = Category(name=cat_name)
    cat.save()
    return cat
