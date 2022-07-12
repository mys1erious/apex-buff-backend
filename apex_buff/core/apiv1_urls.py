from django.urls import path

from legends.api import views as legend_views
from abilities.api import views as ability_views
from weapons.api import views as weapon_views

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
        view=ability_views.AbilityDetailAPIView.as_view(),
        name='abilities'
    ),

    # WeaponAmmo
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

    # WeaponAttachments
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

    # WeaponFiremods
    # {% url 'api:firemods' %}
    path(
        route='firemods/',
        view=weapon_views.FireModeListCreateAPIView.as_view(),
        name='firemods'
    ),
    # {% url 'api:firemods' firemod.slug %}
    path(
        route='firemods/<slug:slug>/',
        view=weapon_views.FireModeRetrieveUpdateDestroyAPIView.as_view(),
        name='firemods'
    ),

    # Weapons
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
    # {% url 'api:weapon_damage' weapon.slug %}
    path(
        route='weapons/<slug:slug>/damage/',
        view=weapon_views.WeaponDamageAPIView.as_view(),
        name='weapon_damage'
    ),
    # {% url 'api:weapon_ammo' weapon.slug %}
    path(
        route='weapons/<slug:slug>/ammo/',
        view=weapon_views.WeaponAmmoAPIView.as_view(),
        name='weapon_ammo'
    ),
    # {% url 'api:weapon_attachments' weapon.slug %}
    path(
        route='weapons/<slug:slug>/attachments/',
        view=weapon_views.WeaponAttachmentAPIView.as_view(),
        name='weapon_attachments'
    ),
    # {% 'api:weapon_firemods' weapon.slug %}
    path(
        route='weapons/<slug:slug>/firemods/',
        view=weapon_views.WeaponFiremodeListAPIView.as_view(),
        name='weapon_firemods'
    ),
    # {% 'api:weapon_firemods' weapon.slug firemode.slug %}
    path(
        route='weapons/<slug:slug>/firemods/<slug:firemode_slug>',
        view=weapon_views.WeaponFiremodeDetailAPIView.as_view(),
        name='weapon_firemods'
    )
]
