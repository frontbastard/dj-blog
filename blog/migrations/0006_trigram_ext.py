# Generated by Django 5.0.9 on 2024-11-26 21:21
from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_post_tags"),
    ]

    operations = [
        TrigramExtension()
    ]
