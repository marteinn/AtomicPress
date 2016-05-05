from sqlalchemy import or_, and_

from atomicpress.app import app
from atomicpress.models import Post, PostStatus


def gen_post_status():
    """
    Show only published posts outside debug.
    """

    if not app.config["DEBUG"]:
        post_status = and_(Post.status == PostStatus.PUBLISH)
    else:
        post_status = or_(Post.status == PostStatus.PUBLISH,
                          Post.status == PostStatus.DRAFT)
    return post_status
