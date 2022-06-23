from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def legend_upload_to(instance, filename):
    return f'legends/{filename}'


def legend_type_upload_to(instance, filename):
    return f'legends/types/{filename}'


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

    icon = models.ImageField(
        upload_to=legend_type_upload_to,
        default='no_image.png',
        blank=True
    )
    slug = models.SlugField(unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('legend_types', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Legend(models.Model):
    class Genders(models.TextChoices):
        MALE = 'm', 'Male'
        FEMALE = 'f', 'Female'
        NON_BINARY = 'nb', 'Non-binary'

    name = models.CharField(
        max_length=50,
        unique=True
    )
    icon = models.ImageField(
        upload_to=legend_upload_to,
        default='no_image.png',
        blank=True
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
        null=True
    )
    lore = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('legends', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
