import os

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings

from cloudinary.models import CloudinaryField


class LegendType(models.Model):
    class Names(models.TextChoices):
        RECON = 'recon', 'Recon'
        DEFENSIVE = 'defensive', 'Defensive'
        OFFENSIVE = 'offensive', 'Offensive'
        SUPPORT = 'support', 'Support'

    name = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        choices=Names.choices,
    )

    icon = CloudinaryField(
        resource_type='image',
        use_filename=True,
        unique_filename=False,
        folder='legends/types/',
        overwrite=False,
        blank=True,
        default='no_image'
    )
    icon_imgf = models.ImageField(
        upload_to='legends/types/',
        default='no_image',
        blank=True
    )

    slug = models.SlugField(unique=True, blank=True)

    @property
    def icon_url(self):
        return f'{settings.STORAGE_BASE_URL}/{self.icon}'

    def get_absolute_url(self):
        return reverse('legend_types', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    # def __unicode__(self):
    #     try:
    #         public_id = self.icon.public_id
    #     except AttributeError:
    #         public_id = ''
    #     return "Photo <%s:%s>" % (self.title, public_id)


class Legend(models.Model):
    class Genders(models.TextChoices):
        MALE = 'm', 'Male'
        FEMALE = 'f', 'Female'
        NON_BINARY = 'nb', 'Non-binary'

    name = models.CharField(
        max_length=50,
        unique=True
    )
    icon = CloudinaryField(
        'image',
        use_filename=True,
        unique_filename=False,
        folder='legends/',
        overwrite=False,
        blank=True,
        default='no_image'
    )
    slug = models.SlugField(unique=True, blank=True)

    role = models.CharField(
        max_length=100,
        blank=True
    )
    real_name = models.CharField(
        max_length=100,
        blank=True
    )
    gender = models.CharField(
        max_length=2,
        choices=Genders.choices
    )
    age = models.IntegerField(
        blank=True,
        null=True
    )
    homeworld = models.CharField(
        max_length=100,
        blank=True
    )
    legend_type = models.ForeignKey(
        to=LegendType,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    lore = models.TextField(blank=True)

    @property
    def icon_url(self):
        return f'{settings.STORAGE_BASE_URL}/{self.icon}'

    def get_absolute_url(self):
        return reverse('legends', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
