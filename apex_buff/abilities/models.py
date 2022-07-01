from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from legends.models import Legend


def upload_to(instance, filename):
    return f'abilities/{filename}'


class Ability(models.Model):
    class AbilityTypes(models.TextChoices):
        TACTICAL = 'tactical', 'Tactical'
        PASSIVE = 'passive', 'Passive'
        ULTIMATE = 'ultimate', 'Ultimate'
        PERK = 'perk', 'Perk'

    slug = models.SlugField(unique=True, blank=True)
    legend = models.ForeignKey(
        to=Legend,
        on_delete=models.CASCADE,
        related_name='abilities'
    )
    name = models.CharField(
        max_length=50,
        default='no_image',
        blank=True,
    )
    description = models.TextField(blank=True)
    info = models.TextField(blank=True)
    icon = models.ImageField(
        upload_to=upload_to,
        blank=True
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

    def get_absolute_url(self):
        return reverse('abilities', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = f'{self.legend.slug}/{slugify(self.name)}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug
