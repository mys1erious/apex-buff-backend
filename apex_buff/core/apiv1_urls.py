from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from legends.api import views as legend_views
from abilities.api import views as ability_views
from weapons.api import views as weapon_views
from user_stats.api import views as user_stat_views


urlpatterns = [
    # -- Abilities --
    # {% url 'api:abilities' %}
    path(
        route='abilities/',
        view=ability_views.AbilityListAPIView.as_view(),
        name='abilities'
    ),
    # {% url 'api:abilities' ability.slug %}
    path(
        route='abilities/<slug:slug>/',
        view=ability_views.AbilityDetailAPIView.as_view(),
        name='abilities'
    ),


    # -- LegendTypes --
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


    # -- Legends --
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
        name='legends-type'
    ),
    # {% url 'api:legends_abilities' legend.slug %}
    path(
        route='legends/<slug:slug>/abilities/',
        view=legend_views.LegendAbilityListAPIView.as_view(),
        name='legends-abilities'
    ),
    # {% url 'api:legends_ability' legend.slug ability.slug %}


    # -- Weapons --
    # {% url 'api:weapons' %}
    path(
        route='weapons/',
        view=weapon_views.WeaponListAPIView.as_view(),
        name='weapons'
    ),
    # {% url 'api:weapons' weapon.slug %}
    path(
        route='weapons/<slug:slug>/',
        view=weapon_views.WeaponDetailAPIView.as_view(),
        name='weapons'
    ),
    # {% url 'api:weapon_attachments' weapon.slug %}
    path(
        route='weapons/<slug:slug>/attachments/',
        view=weapon_views.WeaponAttachmentListAPIView.as_view(),
        name='weapon_attachments'
    ),
    # {% url 'api:weapon_ammo' weapon.slug %}
    path(
        route='weapons/<slug:slug>/ammo/',
        view=weapon_views.WeaponAmmoListAPIView.as_view(),
        name='weapon_ammo'
    ),
    # {% url 'api:weapon_mags' weapon.slug %}
    path(
        route='weapons/<slug:slug>/mags/',
        view=weapon_views.WeaponMagListAPIView.as_view(),
        name='weapon_mags'
    ),
    # {% url 'api:weapon_damage' weapon.slug %}
    path(
        route='weapons/<slug:slug>/damage/',
        view=weapon_views.WeaponDamageAPIView.as_view(),
        name='weapon_damage'
    ),
    # {% 'api:weapon_fire_modes' weapon.slug %}
    path(
        route='weapons/<slug:slug>/fire_modes/',
        view=weapon_views.WeaponFireModeAPIView.as_view(),
        name='weapon_fire_modes'
    ),


    # -- Attachments --
    # {% url 'api:attachments' %}
    path(
        route='attachments/',
        view=weapon_views.AttachmentListCreateAPIView.as_view(),
        name='attachments'
    ),
    # {% url 'api:attachments' attachments.slug %}
    path(
        route='attachments/<slug:slug>/',
        view=weapon_views.AttachmentRetrieveUpdateDestroyAPIView.as_view(),
        name='attachments'
    ),


    # -- Ammo --
    # {% url 'api:ammo' %}
    path(
        route='ammo/',
        view=weapon_views.AmmoListCreateAPIView.as_view(),
        name='ammo'
    ),
    # {% url 'api:ammo' ammo.slug %}
    path(
        route='ammo/<slug:slug>/',
        view=weapon_views.AmmoRetrieveUpdateDestroyAPIView.as_view(),
        name='ammo'
    ),


    # -- FireModes --
    # {% url 'api:fire_modes' %}
    path(
        route='fire_modes/',
        view=weapon_views.FireModeListCreateAPIView.as_view(),
        name='fire_modes'
    ),
    # {% url 'api:fire_modes' fire_mode.slug %}
    path(
        route='fire_modes/<slug:slug>/',
        view=weapon_views.FireModeRetrieveUpdateDestroyAPIView.as_view(),
        name='fire_modes'
    ),


    # -- Modificators --
    # {% url 'api:modificators' %}
    path(
        route='modificators/',
        view=weapon_views.ModificatorListCreateAPIView.as_view(),
        name='modificators'
    ),
    # {% url 'api:modificators' modificator.slug %}
    path(
        route='modificators/<slug:slug>/',
        view=weapon_views.ModificatorRetrieveUpdateDestroyAPIView.as_view(),
        name='modificators'
    ),


    # -- UserStats --
    # {% url 'api:user_token_obtain_pair' %}
    path(
        route='users/token/',
        view=TokenObtainPairView.as_view(),
        name='user_token_obtain_pair'
    ),
    # {% url 'api:user_token_refresh' %}
    path(
        route='users/token/refresh/',
        view=TokenRefreshView.as_view(),
        name='user_token_refresh'
    ),
    # {% url 'api:user_profile' %}
    path(
        route='users/profile/',
        view=user_stat_views.UserProfileAPIView.as_view(),
        name='user_profile'
    ),
]
