from django.db import models
from django.conf import settings

from cloudinary.models import CloudinaryField as BaseCloudinaryField


class CloudinaryField(BaseCloudinaryField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def url(self):
        return f'{settings.CLOUDINARY_ROOT_URL}/{self}'
