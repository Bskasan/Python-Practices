from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/4.2/topics/db/models/#:~:text=A%20model%20is%20the%20single,.db.models.Model%20.

class Student(models.Model):
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.IntegerField()
    is_active = models.BooleanField(default=True)
    # image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True) # Write the time automatically when signed up.
    updated = models.DateTimeField(auto_now=True) # Write the time automaticall when updated.
