from django.db import models, connection
from django.db.models.expressions import RawSQL
from django.urls import reverse
from django.utils.text import slugify

from core.models import (
    CloudinaryIconUrlModel,
)

from cloudinary.models import CloudinaryField


class Modificator(CloudinaryIconUrlModel):
    class Names(models.TextChoices):
        DEFAULT = 'default', 'Default'
        MODDED_LOADER = 'modded loader', 'Modded Loader'
        SNIPER_AMMO_AMPED = 'sniper ammo amped', 'Sniper Ammo Amped'
        DOUBLE_TAP_TRIGGER = 'double tap trigger', 'Double Tap Trigger'
        HEAVY_ROUNDS_REVVED_UP = 'heavy rounds revved up', 'Heavy Rounds Revved Up'
    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(
        max_length=127,
        unique=True,
        choices=Names.choices
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


class RangeStat(models.Model):
    # Add index by name?
    class Names(models.TextChoices):
        PROJECTILE_SPEED = 'projectile speed', 'Projectile Speed',
        BODY_DAMAGE = 'body damage', 'Body Damage',
        HEAD_DAMAGE = 'head damage', 'Head Damage',
        LEGS_DAMAGE = 'legs damage', 'Legs Damage',
        RPM = 'rpm', 'Round Per Minute',
        DPS = 'dps', 'Damage Per Second',
        TTK = 'ttk', 'Time To Kill'

    name = models.CharField(
        max_length=50,
        choices=Names.choices
    )
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)

    def is_range(self):
        return not self.min == self.max

    def value_display(self):
        min = self.min
        max = self.max

        if min.is_integer() and max.is_integer():
            min, max = int(min), int(max)

        if min == max:
            return min
        return f'{min}-{max}'

    def __str__(self):
        res = f'{self.name}: '
        if self.min == self.max:
            res += str(self.min)
        else:
            res += f'{self.min}-{self.max}'

        return res

    class Meta:
        indexes = [models.Index(fields=['name', ])]


class Weapon(CloudinaryIconUrlModel):
    class WeaponTypes(models.TextChoices):
        ASSAULT_RIFLE = 'Assault rifle', 'Assault rifle'
        SMG = 'SMG', 'SMG'
        LMG = 'LMG', 'LMG'
        MARKSMAN_WEAPON = 'Marksmanweapon', 'Marksman weapon'
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
    projectile_speed = models.OneToOneField(
        to=RangeStat,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='projectile_speed'
    )

    @property
    def attachments(self):
        # Rework for faster performance
        attachments = Attachment.objects.filter(
            pk__in=self.weapon_attachments.select_related('attachment').values_list('attachment_id', flat=True)
        )
        return attachments

    def add_attachment(self, attachment):
        new_attachment = WeaponAttachment(weapon=self, attachment=attachment)
        new_attachment.save()

    @property
    def ammo(self):
        # Rework for faster performance
        ammo_ids = WeaponAmmo.objects.filter(weapon=self).values_list('ammo', flat=True)
        ammo = Attachment.objects.filter(pk__in=ammo_ids)
        return ammo

    def add_ammo(self, ammo):
        new_ammo = WeaponAmmo(weapon=self, ammo=ammo)
        new_ammo.save()

    def add_mag(self, modificator, size):
        new_mag = WeaponMag(
            weapon=self,
            modificator=modificator,
            size=size
        )
        new_mag.save()

    @property
    def damage(self):
        damage = WeaponDamage.objects.filter(weapon=self).all()#.select_related('modificator', 'body', 'head', 'legs')
        return damage

    def add_damage(self, modificator, body, head, legs):
        new_damage = WeaponDamage(
            weapon=self,
            modificator=modificator,
            body=body, head=head, legs=legs
        )
        new_damage.save()

    @property
    def fire_modes(self):
        fire_modes = WeaponFireMode.objects.filter(weapon=self).all().select_related(
            'fire_mode',
            'damage_stats__rpm',
            'damage_stats__dps',
            'damage_stats__ttk',
            'damage_stats__modificator'
        )
        return fire_modes

    def add_fire_mode(self, modificator, fire_mode, rpm, dps, ttk):
        new_damage_stats = DamageStats.objects.create(
            modificator=modificator,
            rpm=rpm, dps=dps, ttk=ttk
        )
        new_damage_stats.save()

        new_fire_mode = WeaponFireMode(
            weapon=self,
            fire_mode=fire_mode,
            damage_stats=new_damage_stats
        )
        new_fire_mode.save()

    @staticmethod
    def get_all_weapons():
        weapons = Weapon.objects.select_related(
            'projectile_speed',
        ).prefetch_related(
            'damage__modificator',
            'damage__body',
            'damage__head',
            'damage__legs',
            # 'weapon_attachments__attachment'
        ).all()
        return weapons

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
        on_delete=models.CASCADE,
        related_name='weapon_attachments'
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
        related_name='weapon_ammo'
    )
    ammo = models.ForeignKey(
        to=Ammo,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.weapon.name} --> {self.ammo.name}'


class WeaponMag(models.Model):
    weapon = models.ForeignKey(
        to=Weapon,
        on_delete=models.CASCADE,
        related_name='weapon_mags'
    )
    modificator = models.ForeignKey(
        to=Modificator,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None
    )
    size = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.weapon.name} --> {self.modificator.name} --> {self.size}'


class WeaponDamage(models.Model):
    weapon = models.ForeignKey(
        to=Weapon,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name='damage'
    )
    modificator = models.ForeignKey(
        to=Modificator,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None
    )
    body = models.OneToOneField(
        to=RangeStat,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='body'
    )
    head = models.OneToOneField(
        to=RangeStat,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='head'
    )
    legs = models.OneToOneField(
        to=RangeStat,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='legs'
    )

    def __str__(self):
        return f'{self.weapon.name} --> {self.modificator.name}: {self.body=}, {self.head=}, {self.legs=}'


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


class DamageStats(models.Model):
    modificator = models.ForeignKey(
        to=Modificator,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None
    )
    rpm = models.OneToOneField(
        to=RangeStat,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='rpm'
    )
    dps = models.OneToOneField(
        to=RangeStat,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='dps'
    )
    ttk = models.OneToOneField(
        to=RangeStat,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='ttk'
    )


class WeaponFireMode(models.Model):
    weapon = models.ForeignKey(
        to=Weapon,
        on_delete=models.CASCADE,
        related_name='weapon_fire_modes'
    )
    fire_mode = models.ForeignKey(
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
        return f'{self.weapon.name} - {self.fire_mode.name}'
