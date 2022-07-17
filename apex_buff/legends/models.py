from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from cloudinary.models import CloudinaryField

from abilities.models import Ability
from core.models import CloudinaryIconUrlModel

from .exceptions import TooManyAbilities, AbilityHasOtherLegend


class LegendType(CloudinaryIconUrlModel):
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
        folder='legends/types/',
        use_filename=True,
        unique_filename=False,
        blank=True,
        default='no_image'
    )
    slug = models.SlugField(unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('legend_types', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Legend(CloudinaryIconUrlModel):
    # Not sure how to implement in a better way (to have the same result as Model.DoesNotExist for example)
    TooManyAbilities = TooManyAbilities
    AbilityHasOtherLegend = AbilityHasOtherLegend

    MAX_ABILITIES = 4

    class Genders(models.TextChoices):
        MALE = 'm', 'Male'
        FEMALE = 'f', 'Female'
        NON_BINARY = 'nb', 'Non-binary'

    name = models.CharField(
        max_length=50,
        unique=True
    )
    icon = CloudinaryField(
        resource_type='image',
        folder='legends/',
        use_filename=True,
        unique_filename=False,
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
        null=True,
        default=None
    )
    lore = models.TextField(blank=True)

    def update_legend_type(self, legend_type):
        self.legend_type = legend_type
        self.save()

    def delete_legend_type(self):
        self.legend_type = None
        self.save()

    @staticmethod
    def all_legends():
        return Legend.objects.select_related('legend_type').prefetch_related('abilities').all()

    @property
    def icon_url(self):
        url = self.icon.build_url(raw_transformation='e_bgremoval')
        return url

    def get_absolute_url(self):
        return reverse('legends', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
