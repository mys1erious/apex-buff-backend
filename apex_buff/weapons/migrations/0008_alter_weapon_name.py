# Generated by Django 4.0.6 on 2022-07-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0007_alter_weapon_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='name',
            field=models.CharField(max_length=127, unique=True),
        ),
    ]
