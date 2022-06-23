# Generated by Django 4.0.5 on 2022-06-20 18:14

from django.db import migrations, models
import legends.models


class Migration(migrations.Migration):

    dependencies = [
        ('legends', '0002_alter_legendtype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legend',
            name='icon',
            field=models.ImageField(blank=True, default='no_image.png', upload_to=legends.models.legend_upload_to),
        ),
        migrations.AlterField(
            model_name='legend',
            name='lore',
            field=models.TextField(blank=True),
        ),
    ]
