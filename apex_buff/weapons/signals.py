from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Weapon, WeaponDamage


@receiver(post_delete, sender=Weapon)
def delete_reverse(sender, **kwargs):
    try:
        if kwargs['instance'].projectile_speed:
            kwargs['instance'].projectile_speed.delete()
    except:
        pass


@receiver(post_delete, sender=WeaponDamage)
def delete_reverse(sender, **kwargs):
    try:
        if kwargs['instance'].body:
            kwargs['instance'].body.delete()
        if kwargs['instance'].head:
            kwargs['instance'].head.delete()
        if kwargs['instance'].legs:
            kwargs['instance'].legs.delete()

    except:
        pass
