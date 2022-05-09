# Generated by Django 3.1.1 on 2022-01-16 20:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Profile', '0004_auto_20220116_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='Link_Author',
        ),
        migrations.AddField(
            model_name='links',
            name='Link_Author',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
