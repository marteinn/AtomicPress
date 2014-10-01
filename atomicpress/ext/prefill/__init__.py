# -*- coding: utf-8 -*-

"""
atomicpress.ext.prefill
----------
Insert initial dummy data.

"""

from atomicpress.app import app, db
from atomicpress.models import Blog
from flask_script import Manager

PreFillCommand = Manager(usage='Insert initial dummy data')

@PreFillCommand.command
def fill():
    blog = Blog(title="My Blog", tagline="Hi! And welcome to my blog")
    
    db.session.add(blog)
    db.session.commit()
