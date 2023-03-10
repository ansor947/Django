# Generated by Django 4.1.5 on 2023-02-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('image', models.ImageField(upload_to='image/% Y/% m/% d/', height_field=None, width_field=None, max_length=40)),
                ('release_date', models.DateField()),
                ('lte_exists', models.CharField(max_length=40)),
                ('slug', models.SlugField(max_length=40)),
            ],
        ),
    ]
