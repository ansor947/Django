# Generated by Django 4.1.5 on 2023-02-03 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_alter_phone_image_alter_phone_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=40, unique=True),
        ),
    ]
