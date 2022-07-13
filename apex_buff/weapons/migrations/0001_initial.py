# Generated by Django 4.0.6 on 2022-07-10 14:08

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ammo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(choices=[('arrows', 'Arrows'), ('energy', 'Energy'), ('heavy', 'Heavy'), ('light', 'Light'), ('shotgun', 'Shotgun'), ('sniper', 'Sniper'), ('mythic', 'Mythic')], max_length=20, unique=True)),
                ('icon', cloudinary.models.CloudinaryField(blank=True, default='no_image', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=127, unique=True)),
                ('icon', cloudinary.models.CloudinaryField(blank=True, default='no_image', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FireMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=127, unique=True)),
                ('icon', cloudinary.models.CloudinaryField(blank=True, default='no_image', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=127, unique=True)),
                ('icon', cloudinary.models.CloudinaryField(blank=True, default='no_image', max_length=255)),
                ('weapon_type', models.CharField(blank=True, max_length=50)),
                ('mag_size', models.IntegerField(blank=True, null=True)),
                ('projectile_speed', models.IntegerField(blank=True, null=True)),
                ('ammo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='weapons.ammo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WeaponDamage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.IntegerField(blank=True, null=True)),
                ('head', models.IntegerField(blank=True, null=True)),
                ('legs', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeaponFiremode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firemode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='weapons.firemode')),
                ('weapon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weapons.weapon')),
            ],
        ),
        migrations.CreateModel(
            name='WeaponAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='weapons.attachment')),
                ('weapon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weapons.weapon')),
            ],
        ),
        migrations.AddField(
            model_name='weapon',
            name='damage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='weapons.weapondamage'),
        ),
    ]