# Generated by Django 4.2.5 on 2023-09-11 12:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_admin",
        ),
    ]
