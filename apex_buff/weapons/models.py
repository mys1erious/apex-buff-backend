from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from core.models import (
    CloudinaryIconUrlModel,
)

from cloudinary.models import CloudinaryField


class Weapon(CloudinaryIconUrlModel):
    class WeaponTypes(models.TextChoices):
        ASSAULT_RIFLE = 'Assault rifle', 'Assault rifle'
        SMG = 'SMG', 'SMG'
        LMG = 'LMG', 'LMG'
        MARKSMAN_WEAPON = 'Marksman weapon', 'Marksman weapon'
        SNIPER_RIFLE = 'Sniper rifle', 'Sniper rifle'
        SHOTGUN = 'Shotgun', 'Shotgun'
        PISTOL = 'Pistol', 'Pistol'

    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(
        max_length=127,
        unique=True,
    )
    icon = CloudinaryField(
        resource_type='image',
        folder='weapons/',
        use_filename=True,
        unique_filename=False,
        blank=True,
        default='no_image'
    )
    weapon_type = models.CharField(
        max_length=50,
        choices=WeaponTypes.choices
    )
#     mag_size = models.IntegerField(blank=True, null=True, default=None)
#     projectile_speed = models.IntegerField()
#
#     @property
#     def firemods(self):
#         firemode_slugs = WeaponFiremode.objects.filter(
#             weapon=self
#         ).values_list('firemode__slug', flat=True)
#
#         firemode_slugs_list = list(firemode_slugs)
#         firemods = FireMode.objects.in_bulk(id_list=firemode_slugs_list, field_name='slug')
#
#         return firemods.values()
#
#     @property
#     def weapon_firemods(self):
#         weapon_firemodes = WeaponFiremode.objects.filter(weapon=self)
#         return weapon_firemodes

    # @staticmethod
    # def all_weapons():
    #     return Weapon.objects.select_related('legend_type').prefetch_related('abilities').all()

    @property
    def attachments(self):
        # Rework for faster performance
        attachment_ids = WeaponAttachment.objects.filter(weapon=self).values_list('attachment', flat=True)
        attachments = Attachment.objects.in_bulk(id_list=list(attachment_ids))
        return attachments.values()

    def add_attachment(self, attachment):
        new_attachment = WeaponAttachment(weapon=self, attachment=attachment)
        new_attachment.save()

    @property
    def ammo(self):
        # Rework for faster performance
        ammo_ids = WeaponAmmo.objects.filter(weapon=self).values_list('ammo', flat=True)
        ammo = Ammo.objects.in_bulk(id_list=list(ammo_ids))
        return ammo.values()

    def add_ammo(self, ammo):
        new_ammo = WeaponAmmo(weapon=self, ammo=ammo)
        new_ammo.save()

    @property
    def icon_url(self):
        return self.icon.build_url(raw_transformation='e_trim/e_bgremoval')

    def get_absolute_url(self):
        return reverse('weapons', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Attachment(CloudinaryIconUrlModel):
    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(
        max_length=127,
        unique=True,
        blank=True
    )
    icon = CloudinaryField(
        resource_type='image',
        folder='weapons/attachments/',
        use_filename=True,
        unique_filename=False,
        blank=True,
        default='no_image'
    )

    @property
    def icon_url(self):
        return self.icon.build_url(raw_transformation='e_trim/e_bgremoval')

    def get_absolute_url(self):
        return reverse('attachments', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class WeaponAttachment(models.Model):
    weapon = models.ForeignKey(
        to=Weapon,
        on_delete=models.CASCADE
    )
    attachment = models.ForeignKey(
        to=Attachment,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.weapon.name} --> {self.attachment.name}'


class Ammo(CloudinaryIconUrlModel):
    class Names(models.TextChoices):
        ARROWS = 'Arrows', 'Arrows'
        ENERGY = 'Energy', 'Energy'
        HEAVY = 'Heavy', 'Heavy'
        LIGHT = 'Light', 'Light'
        SHOTGUN = 'Shotgun', 'Shotgun'
        SNIPER = 'Sniper', 'Sniper'
        MYTHIC = 'Mythic', 'Mythic'

    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(
        max_length=20,
        unique=True,
        choices=Names.choices
    )
    icon = CloudinaryField(
        resource_type='image',
        folder='weapons/ammo/',
        use_filename=True,
        unique_filename=False,
        blank=True,
        default='no_image'
    )

    @property
    def icon_url(self):
        return self.icon.build_url(raw_transformation='e_trim/e_bgremoval')

    def get_absolute_url(self):
        return reverse('ammo', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class WeaponAmmo(models.Model):
    weapon = models.ForeignKey(
        to=Weapon,
        on_delete=models.CASCADE,
    )
    ammo = models.ForeignKey(
        to=Ammo,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.weapon.name} --> {self.ammo.name}'


class Modificator(CloudinaryIconUrlModel):
    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(
        max_length=127,
        unique=True
    )
    icon = CloudinaryField(
        resource_type='image',
        folder='weapons/modificators/',
        use_filename=True,
        unique_filename=False,
        blank=True,
        default='no_image'
    )

    def icon_url(self):
        return self.icon.build_url(raw_transformation='e_trim/e_bgremoval')

    def get_absolute_url(self):
        return reverse('modificators', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# class FireMode(CloudinaryIconUrlModel):
#     slug = models.SlugField(unique=True, blank=True)
#     name = models.CharField(
#         max_length=127,
#         unique=True
#     )
#     icon = CloudinaryField(
#         resource_type='image',
#         folder='weapons/firemods/',
#         use_filename=True,
#         unique_filename=False,
#         blank=True,
#         default='no_image'
#     )
#
#     def icon_url(self):
#         return self.icon.build_url(raw_transformation='e_trim/e_bgremoval')
#
#     def get_absolute_url(self):
#         return reverse('firemods', kwargs={'slug': self.slug})
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.name


# class WeaponFireMode(models.Model):
#     weapon = models.ForeignKey(
#         to=Weapon,
#         on_delete=models.CASCADE
#     )
#     firemode = models.ForeignKey(
#         to=FireMode,
#         on_delete=models.CASCADE
#     )
#     damage_stats = models.OneToOneField(
#         to=DamageStats,
#         on_delete=models.CASCADE,
#         blank=True,
#         null=True
#     )
#
#     def __str__(self):
#         return f'{self.weapon.name} - {self.firemode.name}'



# class MagSize(models.Model):
#     weapons



# class RangeStat(models.Model):
#     stat_name = models.CharField(max_length=127)
#     min = models.FloatField(blank=True, null=True)
#     max = models.FloatField(blank=True, null=True)


# class DamageStats(models.Model):
#     rpm_min = models.FloatField(blank=True, null=True, default=None)
#     rpm_max = models.FloatField(blank=True, null=True, default=None)
#     dps_min = models.FloatField(blank=True, null=True, default=None)
#     dps_max = models.FloatField(blank=True, null=True, default=None)
#     ttk_min = models.FloatField(blank=True, null=True, default=None)
#     ttk_max = models.FloatField(blank=True, null=True, default=None)
#
#     def stat_is_range(self, mn, mx):
#         if mn == mx:
#             return True
#         return False
#
#     @property
#     def rpm_is_range(self):
#         return self.stat_is_range(self.rpm_min, self.rpm_max)
#
#     @property
#     def dps_is_range(self):
#         return self.stat_is_range(self.dps_min, self.dps_max)
#
#     @property
#     def ttk_is_range(self):
#         return self.stat_is_range(self.ttk_min, self.ttk_max)


# class WeaponDamage(models.Model):
#     weapon = models.OneToOneField(
#         to=Weapon,
#         on_delete=models.CASCADE,
#         null=True,
#         default=None,
#         related_name='damage'
#     )
#     body = models.IntegerField(blank=True, null=True)
#     head = models.IntegerField(blank=True, null=True)
#     legs = models.IntegerField(blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.weapon.name}: head={self.head}, body={self.body}, legs={self.legs}'
