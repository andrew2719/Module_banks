# Generated by Django 4.2.4 on 2023-08-22 15:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0002_remove_courses_id_remove_progress_progress_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Progress',
            new_name='Mycourses',
        ),
    ]