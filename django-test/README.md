# Django test project

```bash
# venv
virtualenv env
. env/bin/activate

# install django
pip3 install Django --index-url https://pypi.org/simple

# init project
django-admin startproject testsite

# start new app
python3 manage.py startapp polls

# migrate
python3 manage.py makemigration polls
python3 manage.py migrate

# runserver
python3 manage.py runserver
```
