# Django Project Template

This Django project template is to be used with the [related app template](https://github.com/atheiman/app_name). By following the simple usage below you can kickstart your Django development.

## Usage

To create a new Django project named 'My New Project' and its first Django app named 'Some Application', follow these steps:

```shell
# Create and activate a virtualenv
virtualenv my_new_env
source my_new_env/bin/activate

# Install Django
pip install django

# Create your Django project
django-admin.py startproject --template=https://github.com/atheiman/project_name/archive/master.zip my_new_project

# Navigate into your project
cd my_new_project

# Clear out this README to make room for your README
echo "# NEW PROJECT" > README.md

# Create your Django app
django-admin.py startapp --template=https://github.com/atheiman/app_name/archive/master.zip some_application

# Use sed as a template language... I know this is pretty bad, but it works.
find . -type f -exec sed -i '' s/PROJECT\ NAME/My\ New\ Project/g {} +
find . -type f -exec sed -i '' s/project_name/my_new_project/g {} +
find . -type f -exec sed -i '' s/APP\ NAME/Some\ Application/g {} +
find . -type f -exec sed -i '' s/app_name/some_application/g {} +

# If sed returns the error "sed: RE error: illegal byte sequence" on a Mac, set the following environment variables
#export LC_CTYPE=C 
#export LANG=C

# Migrate a local SQLite database
python manage.py migrate

# Run the Django development server
python manage.py runserver
```

[Look at what you have created.](http://127.0.0.1:8000/some_application/)

![Simple front end made with Bootstrap](http://i.imgur.com/4eOf1oH.png)

![Responsive to small screens](http://i.imgur.com/Yx2wf2e.png)
