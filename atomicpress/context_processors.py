from atomicpress.app import app
from flask import request, url_for


def is_showing(route=None, **kwargs):
    url = url_for(route, **kwargs)
    if request.path == url:
        return "active"
    return ""


app.jinja_env.globals.update(is_showing=is_showing)


"""
@app.context_processor
def example(slug=None):
    return {}


app.jinja_env.globals.update(example=example)
"""