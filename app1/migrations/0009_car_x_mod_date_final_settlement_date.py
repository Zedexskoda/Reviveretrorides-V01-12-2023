# Generated by Django 4.2.5 on 2023-10-01 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_remove_car_x_mod_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_x_mod',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='final_settlement',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
