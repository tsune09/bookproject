# Generated by Django 5.2 on 2025-04-12 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0003_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="thumbnail",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
