# Generated by Django 4.2.4 on 2023-08-29 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_courses_course_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycourses',
            name='course',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='App.courses'),
        ),
    ]