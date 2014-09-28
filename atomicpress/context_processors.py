from atomicpress.app import app
from flask import request, url_for


def is_url_showing(route=None, **kwargs):
    url = url_for(route, **kwargs)
    urls = (app.config["FREEZER_BASE_URL"].strip("/")+request.path,
            request.path,)

    if url in urls:
        return "active"
    return ""


app.jinja_env.globals.update(is_url_showing=is_url_showing)

