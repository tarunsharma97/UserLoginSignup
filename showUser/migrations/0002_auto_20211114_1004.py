# Generated by Django 3.2.9 on 2021-11-14 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showUser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='email',
        ),
        migrations.RemoveField(
            model_name='register',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='register',
            name='password2',
        ),
    ]
