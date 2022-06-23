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
    ),
    # {% url 'api:legend_types' %}
    path(
        route='legend_types/',
        view=legend_views.LegendTypeListCreateAPIView.as_view(),
        name='legend_types'
    ),
    # {% url 'api:legend_types' legend_type.slug %}
    path(
        route='legend_types/<slug:slug>/',
        view=legend_views.LegendTypeRetrieveUpdateDestroyAPIView.as_view(),
        name='legend_types'
    )
]
