# Generated by Django 4.0.5 on 2022-06-20 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legends', '0003_alter_legend_icon_alter_legend_lore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legend',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]