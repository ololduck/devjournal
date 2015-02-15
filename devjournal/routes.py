from . import app


@app.route('/')
def index():
    return '<h1>Nothing to see here</h1><p>(For now)</p>'
