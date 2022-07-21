from django.contrib import admin
from .models import (
    Weapon,
    Attachment,
    WeaponAttachment,
    Ammo,
    WeaponAmmo,
    WeaponMag,
    WeaponDamage,
    FireMode,
    WeaponFireMode,
    DamageStats,
    Modificator,
    RangeStat,
)


admin.site.register(Weapon)

admin.site.register(Attachment)
admin.site.register(WeaponAttachment)

admin.site.register(Ammo)
admin.site.register(WeaponAmmo)

admin.site.register(WeaponMag)

admin.site.register(WeaponDamage)

admin.site.register(FireMode)
admin.site.register(WeaponFireMode)
admin.site.register(DamageStats)

admin.site.register(Modificator)
admin.site.register(RangeStat)
