# Django Project Template

This Django project template is to be used with the [related app template](https://github.com/atheiman/app_name). By following the simple usage below you can kickstart your Django development.

## Usage

To create a new Django project named 'My Site' containing two Django apps named 'Blog' and 'Accounts', follow these steps:

```shell
# Create and activate a virtualenv. Install django to the virtualenv
virtualenv my_new_env
source my_new_env/bin/activate
pip install django


# Create your Django project
django-admin.py startproject --template=https://github.com/atheiman/project_name/archive/master.zip my_site

# Navigate into your project
cd my_site

# Clear out this README to make room for your README
echo "# NEW PROJECT" > README.md

# Create your Django apps
django-admin.py startapp --template=https://github.com/atheiman/app_name/archive/master.zip blog
django-admin.py startapp --template=https://github.com/atheiman/app_name/archive/master.zip accounts


# Use sed as a template engine... I know this is pretty bad, but it works.
find . -type f -exec sed -i '' s/PROJECT\ NAME/My\ Site/g {} +
find . -type f -exec sed -i '' s/project_name/my_site/g {} +

find blog -type f -exec sed -i '' s/APP\ NAME/Blog/g {} +
find blog -type f -exec sed -i '' s/app_name/blog/g {} +

find accounts -type f -exec sed -i '' s/APP\ NAME/Accounts/g {} +
find accounts -type f -exec sed -i '' s/app_name/accounts/g {} +

# sed may return the error "sed: RE error: illegal byte sequence" on a Mac.
# set the following environment variables to fix this issue:
# export LC_CTYPE=C
# export LANG=C


# Add your app urls to the ROOT_URLCONF located in conf/urls.py
urlpatterns = patterns('',
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
)


# Add your apps to the INSTALLED_APPS tuple in settings/common.py
INSTALLED_APPS = (
    ...
    'accounts',
    'blog',
)


# Migrate a local SQLite database
python manage.py migrate

# Run the Django development server
python manage.py runserver
```

Look at all you have created, you're off to a good start with a [blog](http://127.0.0.1:8000/blog/) and an [accounts](http://127.0.0.1:8000/accounts/) app!
