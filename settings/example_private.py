# These settings are to be imported to other settings files.
# Copy this example to settings/private.py and replace the values below.
# The new private.py file will not be included in your git repo.



# generate a new secret key and paste the value below:
# http://www.miniwebtool.com/django-secret-key-generator/
#PROD_SECRET_KEY = "replace-this-key"



# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

QA_DB = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'personal_site_db',
        'USER': 'personal_site_user',
        'PASSWORD': 'p3r50nal_5ite_pa55w0rd',
        'HOST': 'host.yourdomain.com',
        'PORT': '5432',
    }
}

PROD_DB = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'personal_site_db',
        'USER': 'personal_site_user',
        'PASSWORD': 'p3r50nal_5ite_pa55w0rd',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
