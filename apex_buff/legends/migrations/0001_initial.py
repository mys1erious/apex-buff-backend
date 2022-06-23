# Generated by Django 4.0.5 on 2022-06-20 14:31

from django.db import migrations, models
import django.db.models.deletion
import legends.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LegendType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('icon', models.ImageField(default='no_image.png', upload_to=legends.models.legend_type_upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='Legend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('icon', models.ImageField(default='no_image.png', upload_to=legends.models.legend_upload_to)),
                ('slug', models.SlugField()),
                ('role', models.CharField(blank=True, max_length=100)),
                ('real_name', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('nb', 'Non-binary')], max_length=2)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('homeworld', models.CharField(blank=True, max_length=100)),
                ('lore', models.TextField()),
                ('legend_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='legends.legendtype')),
            ],
        ),
    ]
