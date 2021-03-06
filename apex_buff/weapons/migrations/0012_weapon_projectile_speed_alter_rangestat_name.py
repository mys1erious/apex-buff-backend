# Generated by Django 4.0.6 on 2022-07-20 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0011_remove_weapon_projectile_speed'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='projectile_speed',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='weapons.rangestat'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rangestat',
            name='name',
            field=models.CharField(choices=[('projectile speed', 'Projectile speed')], max_length=50),
        ),
    ]
