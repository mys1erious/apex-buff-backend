from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Weapon, WeaponDamage, WeaponFireMode, DamageStats


@receiver(post_delete, sender=Weapon)
def delete_projectile_speed_on_weapon_delete(sender, **kwargs):
    try:
        if kwargs['instance'].projectile_speed:
            kwargs['instance'].projectile_speed.delete()
    except:
        pass


@receiver(post_delete, sender=WeaponDamage)
def delete_damage_on_weapon_damage_delete(sender, **kwargs):
    try:
        if kwargs['instance'].body:
            kwargs['instance'].body.delete()
        if kwargs['instance'].head:
            kwargs['instance'].head.delete()
        if kwargs['instance'].legs:
            kwargs['instance'].legs.delete()
    except:
        pass


@receiver(post_delete, sender=WeaponFireMode)
def delete_damage_stats_on_weapon_fire_mode_delete(sender, **kwargs):
    try:
        if kwargs['instance'].damage_stats:
            kwargs['instance'].damage_stats.delete()
    except:
        pass


@receiver(post_delete, sender=DamageStats)
def delete_stat_on_damage_stats_delete(sender, **kwargs):
    try:
        if kwargs['instance'].rpm:
            kwargs['instance'].rpm.delete()
        if kwargs['instance'].dps:
            kwargs['instance'].dps.delete()
        if kwargs['instance'].ttk:
            kwargs['instance'].ttk.delete()
    except:
        pass
