# Generated by Django 3.1.1 on 2022-01-16 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='User_Profile',
        ),
    ]
