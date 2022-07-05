from django.db import models
from django.conf import settings

<<<<<<< HEAD

class CloudinaryIconUrlModel(models.Model):
    class Meta:
        abstract = True

    @property
    def icon_url(self):
        return f'{settings.CLOUDINARY_ROOT_URL}/{self.icon}'
=======
from cloudinary.models import CloudinaryField as BaseCloudinaryField


class CloudinaryField(BaseCloudinaryField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def url(self):
        return f'{settings.CLOUDINARY_ROOT_URL}/{self}'
>>>>>>> 5a4563d2caf7c4a9b78f2d9b9cb775ca9ad31f9f
