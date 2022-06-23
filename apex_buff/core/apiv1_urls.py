from django.urls import path

from legends.api import views as legend_views

urlpatterns = [

    # Legends
    # {% url 'api:legends' %}
    path(
        route='legends/',
        view=legend_views.LegendListAPIView.as_view(),
        name='legends'
    ),
    # {% url 'api:legends' legend.slug %}
    path(
        route='legends/<slug:slug>/',
        view=legend_views.LegendDetailAPIView.as_view(),
        name='legends'
    ),
    # {% url 'api:legends_add_type' legend.slug %}
    path(
        route='legends/<slug:slug>/add-type/',
        view=legend_views.LegendLegendTypeDetailAPIView.as_view(),
        name='legends_add_type'
    ),

    # Legend types
    # {% url 'api:legend_types' %}
    path(
        route='legend_types/',
        view=legend_views.LegendTypeListAPIView.as_view(),
        name='legend_types'
    ),
    # {% url 'api:legend_types' legend_type.slug %}
    path(
        route='legend_types/<slug:slug>/',
        view=legend_views.LegendTypeDetailAPIView.as_view(),
        name='legend_types'
    )
]
