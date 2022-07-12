from django.contrib import admin
from .models import Ammo, Attachment, FireMode, Weapon, WeaponAttachment, WeaponFiremode


admin.site.register(Ammo)
admin.site.register(Attachment)
admin.site.register(FireMode)
admin.site.register(Weapon)
admin.site.register(WeaponAttachment)
admin.site.register(WeaponFiremode)
