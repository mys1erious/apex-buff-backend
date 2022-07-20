from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Weapon


@receiver(post_delete, sender=Weapon)
def delete_reverse(sender, **kwargs):
    try:
        if kwargs['instance'].projectile_speed:
            kwargs['instance'].projectile_speed.delete()
    except:
        pass
