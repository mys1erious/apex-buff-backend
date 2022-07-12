from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from core.models import CloudinaryIconUrlModel

from cloudinary.models import CloudinaryField


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


class DamageStats(models.Model):
    rpm = models.FloatField(blank=True, null=True, default=None)
    dps = models.FloatField(blank=True, null=True, default=None)
    ttk = models.FloatField(blank=True, null=True, default=None)


class FireMode(CloudinaryIconUrlModel):
    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(
        max_length=127,
        unique=True
    )
    icon = CloudinaryField(
        resource_type='image',
        folder='weapons/firemods/',
        use_filename=True,
        unique_filename=False,
        blank=True,
        default='no_image'
    )

    def icon_url(self):
        return self.icon.build_url(raw_transformation='e_trim/e_bgremoval')

    def get_absolute_url(self):
        return reverse('firemods', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


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
    mag_size = models.IntegerField(blank=True, null=True, default=None)
    projectile_speed = models.IntegerField()
    ammo = models.ForeignKey(
        to=Ammo,
        on_delete=models.SET_NULL,
        null=True
    )

    @property
    def firemods(self):
        firemode_slugs = WeaponFiremode.objects.filter(
            weapon=self
        ).values_list('firemode__slug', flat=True)

        firemode_slugs_list = list(firemode_slugs)
        firemods = FireMode.objects.in_bulk(id_list=firemode_slugs_list, field_name='slug')

        return firemods.values()

    @property
    def weapon_firemods(self):
        weapon_firemodes = WeaponFiremode.objects.filter(weapon=self)
        return weapon_firemodes

    @property
    def attachments(self):
        attachment_slugs = WeaponAttachment.objects.filter(
            weapon=self
        ).values_list('attachment__slug', flat=True)

        attachment_slugs_list = list(attachment_slugs)
        attachments = Attachment.objects.in_bulk(id_list=attachment_slugs_list, field_name='slug')

        return attachments.values()

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


class WeaponFiremode(models.Model):
    weapon = models.ForeignKey(
        to=Weapon,
        on_delete=models.CASCADE
    )
    firemode = models.ForeignKey(
        to=FireMode,
        on_delete=models.CASCADE
    )
    damage_stats = models.OneToOneField(
        to=DamageStats,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.weapon.name} - {self.firemode.name}'


class WeaponDamage(models.Model):
    weapon = models.OneToOneField(
        to=Weapon,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name='damage'
    )
    body = models.IntegerField(blank=True, null=True)
    head = models.IntegerField(blank=True, null=True)
    legs = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.weapon.name}: head={self.head}, body={self.body}, legs={self.legs}'


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
        return f'{self.weapon.name} - {self.attachment.name}'


'''
/weapons/ [GET, POST]
/weapons/slug/ [GET, PUT, DELETE]

/weapons/attachments/ [GET, POST]
/weapons/attachments/slug/ [PUT, DELETE]

/weapons/fire-mods/ [GET, POST]
/weapons/fire-mods/slug/ [PUT, DELETE]

/weapons/ammo/ [GET, POST]
/weapons/ammo/slug/ [PUT, DELETE]

/weapons/slug/ammo/ [GET, POST, PUT, DELETE]

/weapons/slug/attachments/ [GET, POST]
/weapons/slug/attachments/attachment-slug/ [PUT, DELETE]

/weapons/slug/fire-mods/ [GET, POST]
/weapons/slug/fire-mods/fire-mode-slug/ [PUT, DELETE]
'''
