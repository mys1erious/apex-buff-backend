# Generated by Django 4.0.6 on 2022-07-10 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0009_alter_weapon_ammo_alter_weapon_mag_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='weapon_type',
            field=models.CharField(choices=[('Assault rifle', 'Assault rifle'), ('SMG', 'SMG'), ('LMG', 'LMG'), ('Marksman weapon', 'Marksman weapon'), ('Sniper rifle', 'Sniper rifle'), ('Shotgun', 'Shotgun'), ('Pistol', 'Pistol')], max_length=50),
        ),
    ]