# Generated by Django 5.0.4 on 2024-05-09 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_women_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
