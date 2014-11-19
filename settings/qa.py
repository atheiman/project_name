# qa settings runs the server locally but connects to the prod database

from .common import *
from .private import QA_DB

DEBUG = True

TEMPLATE_DEBUG = True

DATABASES = QA_DB
