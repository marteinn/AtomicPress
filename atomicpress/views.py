import markdown
from atomicpress.app import app
from atomicpress.models import Post, PostStatus, PostType
from flask import send_from_directory
from sqlalchemy import desc
from werkzeug.contrib.atom import AtomFeed
from flask import request


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOADS_PATH"], filename)


@app.route("/feed/atom/")
def feed_latest_posts():
    feed_url = request.url
    url_root = request.url_root.strip("/")

    if "SITE_URL" in app.config:
        url_root = app.config["SITE_URL"]
        feed_url = "%s%s" % (url_root, request.path)

    feed = AtomFeed("Recent posts", feed_url=feed_url, url=url_root)

    posts = Post.query.order_by(desc(Post.date)).\
        filter(Post.status == PostStatus.PUBLISH).\
        filter(Post.type == PostType.POST)

    for post in posts:
        content = post.content

        if post.markdown:
            content = markdown.markdown(content)

        if post.author:
            author_name = post.author.nicename
        else:
            author_name = "Empty"

        feed.add(post.title, unicode(content),
                 content_type='html',
                 author=author_name,
                 url="%s/%s" % (url_root, post.name),
                 updated=post.date,
                 published=post.modified)

    return feed.get_response()

