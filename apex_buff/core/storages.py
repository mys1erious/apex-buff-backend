import os
import re

import requests

import cloudinary
import cloudinary.api
import cloudinary.uploader

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import Storage
from django.core.files.uploadedfile import UploadedFile


class CloudinaryStorage(Storage):
    def __init__(self):
        self.options = settings.CLOUDINARY_STORAGE_SETTINGS

    def _open(self, name, mode='rb'):
        url = self._get_url(name)

        response = requests.get(url)
        if response.status_code == 404:
            raise IOError
        response.raise_for_status()

        file = ContentFile(response.content)
        file.name = name
        file.mode = mode

        return file

    def _upload(self, name, content):

        folder = os.path.dirname(name)
        if folder:
            self.options['folder'] = folder

        return cloudinary.uploader.upload(content, **self.options)

    def _save(self, name, content):
        content = UploadedFile(content, name)
        response = self._upload(name, content)
        return response['public_id']

    def delete(self, name):
        response = cloudinary.uploader.destroy(name, invalidate=True, resource_type='image')
        return response['result'] == 'ok'

    def exists(self, name):
        url = self._get_url(name)

        response = requests.head(url)
        if response.status_code == 404:
            return False
        response.raise_for_status()
        return True

    def url(self, name):
        return self._get_url(name)

    def _get_url(self, name):
        # For now hardcoded
        cloudinary_resource = cloudinary.CloudinaryImage(name).image(
            transformation=[
                {"raw_transformation": "e_bgremoval,e_bgremoval"}
            ]
        )

        # end = text.find(end_pattern) + len(end_pattern)
        # return text[:end]

        start_pattern = 'http'
        end_pattern = '.png'

        start = cloudinary_resource.find(start_pattern)
        end = cloudinary_resource.find(end_pattern) + len(end_pattern)

        url = cloudinary_resource[start:end]
        return url

    def _normalize_path(self, path):
        if path != '' and not path.endswith('/'):
            path += '/'
        return path

    def _normalize_name(self, name):
        return name.replace('\\', '/')
