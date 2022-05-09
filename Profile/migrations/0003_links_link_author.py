# Generated by Django 3.1.1 on 2022-01-16 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Profile', '0002_remove_profile_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='Link_Author',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
