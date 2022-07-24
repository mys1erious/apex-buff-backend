# Generated by Django 4.0.6 on 2022-07-18 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0002_attachment'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeaponAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weapons.attachment')),
                ('weapon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weapons.weapon')),
            ],
        ),
    ]
