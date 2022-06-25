from django.apps import AppConfig


class LegendsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'legends'

    # def ready(self):
    #     from . import signals
