# Generated by Django 4.0.5 on 2022-06-24 12:37

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LegendType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('recon', 'Recon'), ('defensive', 'Defensive'), ('offensive', 'Offensive'), ('support', 'Support')], max_length=20, unique=True)),
                ('icon', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Legend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('icon', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('role', models.CharField(blank=True, max_length=100)),
                ('real_name', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('nb', 'Non-binary')], max_length=2)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('homeworld', models.CharField(blank=True, max_length=100)),
                ('lore', models.TextField(blank=True)),
                ('legend_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='legends.legendtype')),
            ],
        ),
    ]
