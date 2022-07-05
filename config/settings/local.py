from .base import *

import cloudinary.api


DEBUG = True
EMAIL_BACKEND = 'django.Core.mail.backends.console.EmailBackend'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_env_variable('DB_NAME'),
        'HOST': get_env_variable('DB_HOST'),
        'PORT': get_env_variable('DB_PORT'),
        'USER': get_env_variable('DB_USER'),
        'PASSWORD': get_env_variable('DB_PASSWORD')
    }
}


INSTALLED_APPS += ['debug_toolbar', 'cloudinary']


CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS += ['127.0.0.1', 'localhost']


# Cloudinary
cloudinary.config(
  cloud_name=get_env_variable('CLOUDINARY_CLOUD_URL'),
  api_key=get_env_variable('CLOUDINARY_API_KEY'),
  api_secret=get_env_variable('CLOUDINARY_API_SECRET')
)

# Debug Toolbar
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]


INTERNAL_IPS = [
    '127.0.0.1',
    'localhost'
]


DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]
