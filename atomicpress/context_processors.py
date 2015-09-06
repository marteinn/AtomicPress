from atomicpress.app import app
from flask import request, url_for


def is_url_showing(route=None, **kwargs):
    url = url_for(route, **kwargs).strip("/")
    freeze_url = app.config["FREEZER_BASE_URL"].strip("/")+request.path
    urls = (freeze_url.strip("/"),
            request.path.strip("/"),)

    if url in urls:
        return "active"
    return ""


app.jinja_env.globals.update(is_url_showing=is_url_showing)


def is_debug():
    return app.config["DEBUG"]


app.jinja_env.globals.update(is_debug=is_debug)
