# Generated by Django 4.0.6 on 2022-07-18 15:37

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=127, unique=True)),
                ('icon', cloudinary.models.CloudinaryField(blank=True, default='no_image', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]