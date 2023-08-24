# Generated by Django 4.2.4 on 2023-08-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_instructor_student_remove_customuser_education_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('instructor', 'Instructor')], default='student', max_length=10),
        ),
    ]
