from django.urls import path

from legends.api import views as legend_views


urlpatterns = [
    # {% url 'api:legends' %}
    path(
        route='legends/',
        view=legend_views.LegendListCreateAPIView.as_view(),
        name='legends'
    ),
    # {% url 'api:legends' legend.slug %}
    path(
        route='legends/<slug:slug>/',
        view=legend_views.LegendRetrieveUpdateDestroyAPIView.as_view(),
        name='legends'
    )
]
