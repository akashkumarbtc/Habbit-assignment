# Generated by Django 3.2.5 on 2021-07-09 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0003_enrollment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='enrolled_users',
        ),
    ]