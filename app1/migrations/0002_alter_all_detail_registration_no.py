# Generated by Django 4.2.5 on 2023-09-29 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_detail',
            name='registration_no',
            field=models.CharField(max_length=50),
        ),
    ]