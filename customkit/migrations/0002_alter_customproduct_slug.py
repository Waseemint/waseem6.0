# Generated by Django 5.0.1 on 2024-02-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customkit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customproduct',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]