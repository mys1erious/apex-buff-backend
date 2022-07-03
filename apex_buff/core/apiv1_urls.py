from django.urls import path

from legends.api import views as legend_views
from abilities.api import views as ability_views

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
    # {% url 'api:legends_type' legend.slug %}
    path(
        route='legends/<slug:slug>/type/',
        view=legend_views.LegendLegendTypeDetailAPIView.as_view(),
        name='legends_type'
    ),
    # {% url 'api:legends_abilities' legend.slug %}
    path(
        route='legends/<slug:slug>/abilities/',
        view=legend_views.LegendAbilityListAPIView.as_view(),
        name='legends_abilities'
    ),
    # {% url 'api:legends_ability' legend.slug ability.slug%}

    # LegendTypes
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
    ),

    # Abilities
    # {% url 'api:abilities' %}
    path(
        route='abilities/',
        view=ability_views.AbilityListAPIView.as_view(),
        name='abilities'
    ),
    # {% url 'api:abilities' ability.slug %}
    path(
        route='abilities/<slug:slug>/',
        view=ability_views.AbilityDetailAPIView().as_view(),
        name='abilities'
    )
]
