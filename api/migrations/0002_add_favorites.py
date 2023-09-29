# Generated by Django 3.2 on 2023-09-29 17:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorited_races', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='race',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='races_participated', through='api.RaceRegistration', to=settings.AUTH_USER_MODEL),
        ),
    ]
