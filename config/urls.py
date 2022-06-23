from django.contrib import admin
from django.urls import path, include

from core import apiv1_urls

urlpatterns = [
    path(
        route='api/v1/',
        view=include(apiv1_urls),
        name='api'
    ),

    path(
        route='__debug__/',
        view=include('debug_toolbar.urls')
    ),
    path('admin/', admin.site.urls),
]
