# -*- coding: utf-8 -*-

import re

import requests
import markdown

from app import app


IMAGE_MATCH = re.compile("\[(image|img).src=\"(.*?)\"\]",
                         re.MULTILINE | re.DOTALL)
UPLOADS_MATCH = re.compile("\[uploads\]")
GIST_MATCH = re.compile("\[gist.id=(\w*?)\]")
CODE_MATCH = re.compile(r"\[code[^\]]*](.+?)\[/code\]",
                        re.MULTILINE | re.DOTALL)

_gist_cache = {}


@app.template_filter('markdown_content')
def markdown_filter(s):
    extensions = app.config["MARKDOWN_EXTENSIONS"]
    s = markdown.markdown(s, extensions=extensions)
    return s


@app.template_filter('code')
def code_filter(s):
    s = "\n".join(s.splitlines())
    s = re.sub(CODE_MATCH, _handle_code, s)
    return s


def _handle_code(s):
    code = s.groups(1)[0]
    return '<pre class="code">%s</pre>' % code


@app.template_filter('gist')
def gist_filter(s):
    s = re.sub(GIST_MATCH, _handle_gist, s)
    return s


def _handle_gist(s):
    gist_id = s.groups(2)[0]
    raw_content = ""

    # Load data for backend rendering (and seo)
    if app.config["GIST_BACKEND_RENDERING"]:
        if gist_id not in _gist_cache:
            result = requests.get("https://api.github.com/gists/%s" % gist_id,
                                  timeout=30)

            gist = result.json()

            for gist_file in gist.get("files"):
                file_content = gist.get("files").get(gist_file)
                raw_content += file_content.get("content")

            _gist_cache[gist_id] = raw_content
        else:
            raw_content = _gist_cache[gist_id]

    return '<script src="https://gist.github.com/%s.js">' \
           '<noscript><pre>%s</pre></noscript></script>' \
           % (gist_id,
              raw_content)


@app.template_filter('image')
def image_filter(s):
    s = re.sub(IMAGE_MATCH, _handle_image, s)
    s = re.sub(UPLOADS_MATCH, app.config["UPLOADS_URL"]+"/", s)
    return s


def _handle_image(s):
    file_name = s.groups(1)[1]
    uploads_url = app.config["UPLOADS_URL"]
    return "%s/%s" % (uploads_url, file_name)
