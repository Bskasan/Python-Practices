# Decouple for SECRET_KEY
1 - pip install python=decouple
2 - from decouple import confit --> settings.py
3 - SELECT_KEY = config('SECRET_KEY')
4 - Create .env file globally in your local doc
5 - Copy and paste your secret key without '' .

# Don't forget to add your app to installed apps in main/settings.py

# Download Django Rest Framework
= pip install djangorestframework

# Pattern
Model ---> Serializer ---> View ---> Url

# Downloading modules from requirements.txt
- pip install -r requirements.txt