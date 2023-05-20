# Generated by Django 4.2.1 on 2023-05-20 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0004_customer_alter_student_email_alter_student_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.PositiveIntegerField(blank=True, choices=[(10, 'Age = 10'), (20, 'Age = 20'), (30, 'Age = 30'), (40, 'Age = 40'), (50, 'Age = 50')], default=0, null=True),
        ),
    ]