from atomicpress.app import app
from flask import request, url_for


def is_url_showing(route=None, **kwargs):
    url = url_for(route, **kwargs)
    if request.path == url:
        return "active"
    return ""


app.jinja_env.globals.update(is_url_showing=is_url_showing)

