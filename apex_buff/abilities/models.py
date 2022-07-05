from cloudinary.models import CloudinaryField

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from core.models import CloudinaryIconUrlModel
from legends.models import Legend


def upload_to(instance, filename):
    return f'abilities/{filename}'


class Ability(CloudinaryIconUrlModel):
    class AbilityTypes(models.TextChoices):
        TACTICAL = 'tactical', 'Tactical'
        PASSIVE = 'passive', 'Passive'
        ULTIMATE = 'ultimate', 'Ultimate'
        PERK = 'perk', 'Perk'

    slug = models.SlugField(
        unique=True,
        blank=True
    )
    legend = models.ForeignKey(
        to=Legend,
        on_delete=models.CASCADE,
        related_name='abilities'
    )
    name = models.CharField(
        max_length=50,
        blank=True
    )
    description = models.TextField(blank=True)
    info = models.TextField(blank=True)
    icon = CloudinaryField(
        resource_type='image',
        folder='abilities/',
        use_filename=True,
        unique_filename=False,
        blank=True,
        default='no_image'
    )
    ability_type = models.CharField(
        max_length=10,
        choices=AbilityTypes.choices,
    )
    cooldown = models.IntegerField(
        blank=True,
        null=True,
        help_text='Ability cooldown in seconds'
    )

    @property
    def icon_url(self):
        url = self.icon.build_url(raw_transformation='e_trim/e_bgremoval')
        return url

    def get_absolute_url(self):
        return reverse('abilities', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = f'{self.legend.slug}_{slugify(self.name)}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug
