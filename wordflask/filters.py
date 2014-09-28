from app import app
import re
import requests
import markdown


gist_match = re.compile("\[gist.id=(\w*?)\]")
code_match = re.compile(r"\[code[^\]]*](.+?)\[/code\]",
                        re.MULTILINE | re.DOTALL)


@app.template_filter('markdown_content')
def markdown_filter(s):
    s = markdown.markdown(s)
    return s


@app.template_filter('code')
def code_filter(s):
    s = "\n".join(s.splitlines())
    s = re.sub(code_match, _handle_code, s)
    return s


def _handle_code(s):
    code = s.groups(1)[0]
    return '<pre class="code">%s</pre>' % code


@app.template_filter('gist')
def gist_filter(s):
    s = re.sub(gist_match, _handle_gist, s)
    return s


def _handle_gist(s):
    gist_id = s.groups(2)[0]
    raw_content = ""

    result = requests.get("https://api.github.com/gists/%s" % gist_id,
                          timeout=30)

    gist = result.json()

    for gist_file in gist.get("files"):
        file_content = gist.get("files").get(gist_file)
        raw_content += file_content.get("content")

    return '<script src="https://gist.github.com/%s.js">' \
           '<noscript><pre>%s</pre></noscript></script>' \
           % (gist_id,
              raw_content)


