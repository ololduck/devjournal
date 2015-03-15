"""
all the render functions
"""
from .models import ProjectPage, EventPage, Page, Category


def render_project_page(page):
    assert type(page) == ProjectPage
    pass


def render_event_page(page):
    assert type(page) == EventPage
    pass


def get_page_and_type(page_name):
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
    cat = Category.query.filter_by(name=cat_name).first()
    if cat:
        return cat
    cat = Category(name=cat_name)
    cat.save()
    return cat