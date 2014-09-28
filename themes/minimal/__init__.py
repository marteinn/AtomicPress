#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
{{blog_system}}.minimal
----------
A basic {{blog_system}} theme.

"""

from flask import Blueprint


__title__ = 'minimal'
__version__ = '1.0'
__build__ = 10
__author__ = 'Martin Sandström'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014 Martin Sandström'


minimal = Blueprint('minimal', __name__,
                    static_folder="static/builds",
                    static_url_path='/static/minimal',
                    template_folder='templates')

PAGE_SIZE = 10
GA_TRACKING = ""

import views

