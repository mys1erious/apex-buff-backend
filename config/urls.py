from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny

from rest_framework.schemas import get_schema_view

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
        view=get_schema_view(
            title='Schema for Apex Buff',
            description='Schema for API of Apex Legends (not official)',
            version='1.0.0',
            permission_classes=(AllowAny, )
        ),
        name='schema'
    ),
    path(
        route='__debug__/',
        view=include('debug_toolbar.urls')
    ),
    path('admin/', admin.site.urls),
]
