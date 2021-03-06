# Generated by Django 3.2.5 on 2021-07-10 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('syllabus', '0008_auto_20210710_1759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='course',
            new_name='enrolled_course',
        ),
        migrations.RenameField(
            model_name='wishlist',
            old_name='course',
            new_name='wishlist_course',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='enrolled_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='wishlist_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='wishlist_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
