# Generated by Django 4.0.6 on 2022-07-05 17:15

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('legends', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('name', models.CharField(blank=True, default='no_image', max_length=50)),
                ('description', models.TextField(blank=True)),
                ('info', models.TextField(blank=True)),
                ('icon', cloudinary.models.CloudinaryField(blank=True, default='no_image', max_length=255)),
                ('ability_type', models.CharField(choices=[('tactical', 'Tactical'), ('passive', 'Passive'), ('ultimate', 'Ultimate'), ('perk', 'Perk')], max_length=10)),
                ('cooldown', models.IntegerField(blank=True, help_text='Ability cooldown in seconds', null=True)),
                ('legend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abilities', to='legends.legend')),
            ],
        ),
    ]
