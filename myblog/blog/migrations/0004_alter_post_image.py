# Generated by Django 4.1.6 on 2023-02-08 18:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(default="blog/default.jpg", upload_to="blog/"),
        ),
    ]
