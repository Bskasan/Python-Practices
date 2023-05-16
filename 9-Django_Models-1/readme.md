Models-1

# Installing Django and Setting up Environment for Backend
1. python -m venv env
2. Add .gitignore from gitignore.io
3. source env/Scripts/activate
4. pip install django
5. pip freeze
6. pip freeze > requirements.txt for modules and packages. (Package.json for Django)

# Creating app and project
7. django-admin startproject main . -> Creating project ( Don't forget '.' )
8. django-admin startapp fscohort   -> Creating app

# Run Server
9. python manage.py runserver


# Creating Sample For Runserver Page

Import Httpresponse from Django.

from django.http import HttpResponse

def home(request):
    return HttpResponse('''
        Welcome to Home
    ''')
