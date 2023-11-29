# Generated by Django 4.2.6 on 2023-11-22 01:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tweets", "0002_reply"),
    ]

    operations = [
        migrations.AddField(
            model_name="tweet",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="liked_tweets", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]