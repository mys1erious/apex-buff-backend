from .base import *

import django_on_heroku

import cloudinary
import cloudinary.uploader
import cloudinary.api


DEBUG = True


INSTALLED_APPS += ['cloudinary']


ALLOWED_HOSTS += ['apex-buff-development.herokuapp.com']


cloudinary.config(
  cloud_name=os.getenv('CLOUDINARY_CLOUD_URL'),
  api_key=os.getenv('CLOUDINARY_API_KEY'),
  api_secret=os.getenv('CLOUDINARY_API_SECRET')
)


django_on_heroku.settings(locals())
