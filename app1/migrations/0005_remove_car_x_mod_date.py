# Generated by Django 4.2.5 on 2023-09-29 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_work_car_x_mod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_x_mod',
            name='date',
        ),
    ]
