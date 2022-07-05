import os

from django.db import models
from django.conf import settings


class CloudinaryIconUrlModel(models.Model):
    class Meta:
        abstract = True

    @property
    def icon_url(self):
        return f'{settings.CLOUDINARY_ROOT_URL}/{self.icon}'
