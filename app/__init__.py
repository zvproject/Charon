from flask import Flask

app = Flask(__name__)

import os
APP_ROOT = os.path.dirname(os.path.abspath("__file__"))   # refers to application_top
APP_SOURCE = os.path.join(APP_ROOT, 'app/source' )
APP_STATIC = os.path.join(APP_ROOT, 'app/static')

from app import views
