# prod is for running the server on the production webserver

from .common import *
from .private import PROD_DB, PROD_SECRET_KEY

SECRET_KEY = PROD_SECRET_KEY

DEBUG = False

TEMPLATE_DEBUG = False

# list of hostnames that your application will respond to
#ALLOWED_HOSTS = ['*.yourdomain.com', 'app.anotherdomain.org']

DATABASES = PROD_DB
