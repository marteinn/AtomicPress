from flask import Blueprint

__author__ = 'martinsandstrom'

minimal = Blueprint('minimal', __name__,
                    static_folder="static/builds",
                    static_url_path='/static/minimal',
                    template_folder='templates')

PAGE_SIZE = 10

import views

