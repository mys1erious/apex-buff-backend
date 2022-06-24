import os

from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView

from core import apiv1_urls


urlpatterns = [
    path(
        route='api/v1/',
        view=include(apiv1_urls),
        name='api'
    ),
    path(
        route='',
        view=lambda request: redirect('documentation')
    ),

    path(
        route='documentation/',
        view=TemplateView.as_view(
            template_name='swagger-ui.html',
            extra_context={'schema_url': 'schema'},
        ),
        name='documentation'
    ),
    path(
        route='schema/',
        view=SpectacularAPIView.as_view(),
        name='schema'
    ),
    path(
        route='__debug__/',
        view=include('debug_toolbar.urls')
    ),
    path('admin/', admin.site.urls),
]


# Only for local/heroku dev testing (for now)
if os.getenv('DJANGO_SETTINGS_MODULE') == 'config.settings.local':
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
