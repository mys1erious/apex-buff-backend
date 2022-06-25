from .base import *

import django_on_heroku

import cloudinary
import cloudinary.uploader
import cloudinary.api


DEBUG = True


INSTALLED_APPS += ['cloudinary']


ALLOWED_HOSTS += ['apex-buff-development.herokuapp.com']


CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    "localhost:5000",
    "127.0.0.1:5000"
]


cloudinary.config(
  cloud_name=os.getenv('CLOUDINARY_CLOUD_URL'),
  api_key=os.getenv('CLOUDINARY_API_KEY'),
  api_secret=os.getenv('CLOUDINARY_API_SECRET')
)


django_on_heroku.settings(locals())
