from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/4.2/topics/db/models/#:~:text=A%20model%20is%20the%20single,.db.models.Model%20.

class Student(models.Model):
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(default='none@gmail.com', null=True, blank=True)
    number = models.IntegerField(default=0, null=True, blank=True)
    picture = models.ImageField(upload_to='images/', default='', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    # image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True) # Write the time automatically when signed up.
    updated = models.DateTimeField(auto_now=True) # Write the time automaticall when updated.

    def __str__(self):
        return f'{self.first_name} {self.last_name} # {self.number}'

    class Meta: # Change Default Settings
        # https://docs.djangoproject.com/en/4.2/ref/models/options/
        verbose_name = 'Developer'
        verbose_name_plural = "Developers"
        ordering = ["number"] # use '-' for reverse the order 

#--------------------- Django Shell -----------------------#

AGES = (
    (10, 'Age = 10'),
    (20, 'Age = 20'),
    (30, 'Age = 30'),
    (40, 'Age = 40'),
    (50, 'Age = 50'),
)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0, blank=True, null=True, choices=AGES)

    def __str__(self):
        return f'{self.first_name} {self.last_name} = {self.age}'

    # QuerySets: (get, filter, exclude):
    # https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups



