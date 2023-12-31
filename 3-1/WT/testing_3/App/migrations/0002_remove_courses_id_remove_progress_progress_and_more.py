# Generated by Django 4.2.4 on 2023-08-22 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='id',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='progress',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='user',
        ),
        migrations.AddField(
            model_name='courses',
            name='instructor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='courses',
            name='no_of_assignments',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='progress',
            name='no_of_assignmetns_completed',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='progress',
            name='student_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_code',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='progress',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='App.courses'),
        ),
    ]
