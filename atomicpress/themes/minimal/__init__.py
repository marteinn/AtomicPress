#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
atomicpress.themes.minimal
----------
A basic atomicpress theme.

"""

from flask import Blueprint


__title__ = 'minimal'
__version__ = '1.0.1'
__build__ = 101
__author__ = 'Martin Sandström'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014-2015 Martin Sandström'


PAGE_SIZE = 10
GA_TRACKING = ""

theme = Blueprint('minimal', __name__,
                  static_folder="static/builds",
                  static_url_path='/static/minimal',
                  template_folder='templates')

import views
