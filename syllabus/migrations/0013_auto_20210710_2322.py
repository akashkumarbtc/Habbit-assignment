# Generated by Django 3.2.5 on 2021-07-10 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0012_rename_enrolled_user_enrollment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
    ]