from django.db import models

# Our Models
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    