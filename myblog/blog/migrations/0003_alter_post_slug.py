# Generated by Django 4.1.6 on 2023-08-10 09:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_post_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(default="", max_length=200, unique=True),
        ),
    ]