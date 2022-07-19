from django.contrib import admin
from .models import (
    Weapon,
    Attachment,
    WeaponAttachment,
    Ammo,
    WeaponAmmo,
#   FireMode,
#   WeaponFiremode,
    Modificator
#   RangeStat,
#   DamageStats
)


admin.site.register(Weapon)

admin.site.register(Attachment)
admin.site.register(WeaponAttachment)

admin.site.register(Ammo)
admin.site.register(WeaponAmmo)

# admin.site.register(FireMode)
# # admin.site.register(WeaponFireMode)

admin.site.register(Modificator)
# admin.site.register(RangeStat)

# # admin.site.register(DamageStats)
