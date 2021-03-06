# Generated by Django 4.0.6 on 2022-07-24 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0020_alter_damagestats_modificator_alter_rangestat_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='damagestats',
            name='modificator',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='weapons.modificator'),
        ),
        migrations.AlterField(
            model_name='weaponammo',
            name='weapon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weapon_ammo', to='weapons.weapon'),
        ),
        migrations.AlterField(
            model_name='weapondamage',
            name='modificator',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='weapons.modificator'),
        ),
        migrations.AlterField(
            model_name='weaponmag',
            name='modificator',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='weapons.modificator'),
        ),
        migrations.AlterField(
            model_name='weaponmag',
            name='weapon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weapon_mags', to='weapons.weapon'),
        ),
    ]
