# Generated by Django 4.2.5 on 2023-11-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="role",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
