# Generated by Django 3.2.9 on 2021-11-14 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showUser', '0002_auto_20211114_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='email',
            field=models.CharField(default='', max_length=30),
        ),
    ]