# Generated by Django 3.2.9 on 2021-12-01 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showUser', '0003_register_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='profile_image',
            field=models.ImageField(default='images/user1.jpg', null=True, upload_to='images'),
        ),
    ]
