# ToDo API Project

- python --version -> version check for python.

1. python -m venv env
2. source env/Scripts/activate
3. touch .gitignore(create documents 'touch' - Linux command)
4. pip install djangorestframework
5. pip install python-decouple
6. pip freeze > requirements.txt
7. django-admin startproject main .
8. django-admin startapp todo ( app_name )
9. echo SECRET_KEY=django-insecure-k+ls=urs+*6_gp@whg=lz_9%5i%xcpblw6qzaj_44+-f22c-xy > .env
10. Make decouple config settings for SECRET_KEY

# Industry Standart - That means do not touch this code.

    PRIORITY = (
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low')
    )

# ORDER WHEN WE WRITE OUR DJANGO CODE

Model >>> Serializer >>> Views >>> Urls

# ORDER WHEN WE RUN THE CODE

Urls >>> Views >>> Serializer >>> Model

# WHAT IS THE DIFFERENCE BETWEEN PATCH AND PUT HTTP REQUESTS ?

https://www.geeksforgeeks.org/difference-between-put-and-patch-request/

