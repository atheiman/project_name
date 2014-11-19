# NEW PROJECT

## Usage

To create a new Django project named 'My Project' and its first Django app named 'Some Application', follow these steps:

```shell
django-admin.py startproject --template=https://github.com/atheiman/project_name/archive/master.zip my_project
cd my_project
django-admin.py startapp --template=https://github.com/atheiman/app_name/archive/master.zip some_application

find . -type f -exec sed -i '' s/PROJECT\ NAME/My\ Project/g {} +
find . -type f -exec sed -i '' s/project_name/my_project/g {} +
find . -type f -exec sed -i '' s/APP\ NAME/Some\ Application/g {} +
find . -type f -exec sed -i '' s/app_name/some_application/g {} +

python manage.py migrate

python manage.py runserver
```

[See what you have created.](http://127.0.0.1:8000/some_application/)
