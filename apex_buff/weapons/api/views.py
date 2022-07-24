from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions import IsAdminOrReadOnly
from core.utils.response_messages import Context, Messages

from ..models import (
    Weapon,
    Attachment,
    Ammo,
    WeaponDamage,
    FireMode,
    Modificator,
    RangeStat,
)
from .serializers import (
    WeaponSerializer,
    AttachmentSerializer,
    AmmoSerializer,
    MagSerializer,
    DamageSerializer,
    ModificatorSerializer,
    FireModeSerializer,
    WeaponFireModeSerializer
)


class AttachmentListCreateAPIView(ListCreateAPIView):
    queryset = Attachment.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = AttachmentSerializer
    lookup_field = 'slug'


class AttachmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Attachment.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = AttachmentSerializer
    lookup_field = 'slug'


class AmmoListCreateAPIView(ListCreateAPIView):
    queryset = Ammo.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = AmmoSerializer
    lookup_field = 'slug'


class AmmoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ammo.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = AmmoSerializer
    lookup_field = 'slug'


class FireModeListCreateAPIView(ListCreateAPIView):
    queryset = FireMode.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = FireModeSerializer
    lookup_field = 'slug'


class FireModeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FireMode.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = FireModeSerializer
    lookup_field = 'slug'


class ModificatorListCreateAPIView(ListCreateAPIView):
    queryset = Modificator.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = ModificatorSerializer
    lookup_field = 'slug'


class ModificatorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Modificator.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = ModificatorSerializer
    lookup_field = 'slug'


class WeaponListAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, *args, **kwargs):

        weapons = Weapon.objects.all()
        serializer = WeaponSerializer(weapons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = WeaponSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WeaponDetailAPIView(APIView):
    # Add DELETE methods
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, slug, format=None):
        weapon = get_object_or_404(Weapon, slug=slug)
        serializer = WeaponSerializer(weapon, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Is it okay to use partial in PUT or should it be moved ti PATCH?
    def put(self, request, slug, format=None):
        context = Context()
        weapon = get_object_or_404(Weapon, slug=slug)

        serializer = WeaponSerializer(weapon, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            context['message'] = Messages.SUCCESS['PUT'](obj='Weapon', name=weapon.name)
            context['data'] = serializer.data
            return Response(context, status=status.HTTP_200_OK)

        context['message'] = Messages.ERROR['PUT'](obj='Weapon', name=weapon.name)
        context['errors'] = serializer.errors
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


# ---
# Make Detail Views for Weapon dependencies(attachment, ammo, mag, damage, fire_mode) ?
# ---


class WeaponAttachmentListAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, slug, *args, **kwargs):
        weapon = get_object_or_404(Weapon, slug=slug)
        serializer = AttachmentSerializer(weapon.attachments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug, *args, **kwargs):
        context = Context()

        weapon = get_object_or_404(Weapon, slug=slug)
        attachment = get_object_or_404(Attachment, slug=request.data['attachment_slug'])

        weapon.add_attachment(attachment)

        context['message'] = Messages.SUCCESS['POST'](obj='WeaponAttachment', name=weapon.name)
        context['data'] = WeaponSerializer(weapon).data
        return Response(context, status=status.HTTP_200_OK)


class WeaponAmmoListAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, slug, *args, **kwargs):
        weapon = get_object_or_404(Weapon, slug=slug)
        serializer = AmmoSerializer(weapon.ammo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug, *args, **kwargs):
        context = Context()

        weapon = get_object_or_404(Weapon, slug=slug)
        ammo = get_object_or_404(Ammo, slug=request.data['ammo_slug'])

        weapon.add_ammo(ammo)

        context['message'] = Messages.SUCCESS['POST'](obj='WeaponAmmo', name=weapon.name)
        context['data'] = WeaponSerializer(weapon).data
        return Response(context, status=status.HTTP_200_OK)


class WeaponMagListAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, slug, *args, **kwargs):
        weapon = get_object_or_404(Weapon, slug=slug)
        serializer = MagSerializer(weapon.mags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug, *args, **kwargs):
        context = Context()

        weapon = get_object_or_404(Weapon, slug=slug)

        try:
            modificator_slug = request.data['modificator_slug']
        except KeyError:
            context['message'] = Messages.ERROR['POST'](obj='WeaponMag', name=weapon.name)
            context['detail'] = 'modificator_slug wasn`t provided.'
            return Response(context, status=status.HTTP_200_OK)

        modificator = get_object_or_404(Modificator, slug=modificator_slug)
        size = request.data['size']

        weapon.add_mag(modificator, size)

        context['message'] = Messages.SUCCESS['POST'](obj='WeaponMag', name=weapon.name)
        context['data'] = WeaponSerializer(weapon).data
        return Response(context, status=status.HTTP_200_OK)


class WeaponDamageAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, slug, format=None):
        weapon = get_object_or_404(Weapon, slug=slug)
        serializer = DamageSerializer(weapon.damage, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug, format=None):
        context = Context()

        weapon = get_object_or_404(Weapon, slug=slug)

        try:
            modificator_slug = request.data['modificator_slug']
        except KeyError:
            context['message'] = Messages.ERROR['POST'](obj='WeaponDamage', name=weapon.name)
            context['detail'] = 'modificator_slug wasn`t provided.'
            return Response(context, status=status.HTTP_200_OK)

        modificator = get_object_or_404(Modificator, slug=modificator_slug)

        # Move the logic out of view ?
        damage_keys = ['body', 'head', 'legs']
        damage_instances = []
        for key in damage_keys:
            cur_data = request.data[key]
            cur_damage = RangeStat.objects.create(
                name=f'{key} damage',
                min=cur_data['min'],
                max=cur_data['max']
            )
            damage_instances.append(cur_damage)

        weapon.add_damage(
            modificator=modificator,
            body=damage_instances[0],
            head=damage_instances[1],
            legs=damage_instances[2],
        )

        context['message'] = Messages.SUCCESS['POST'](obj='WeaponDamage', name=weapon.name)
        context['data'] = WeaponSerializer(weapon).data
        return Response(context, status=status.HTTP_200_OK)


class WeaponFireModeAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, slug, format=None):
        weapon = get_object_or_404(Weapon, slug=slug)
        serializer = WeaponFireModeSerializer(weapon.fire_modes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug, format=None):
        context = Context()

        weapon = get_object_or_404(Weapon, slug=slug)

        # Move logic out of view, rework to keep dry?
        try:
            modificator_slug = request.data['modificator_slug']
        except KeyError:
            context['message'] = Messages.ERROR['POST'](obj='WeaponDamage', name=weapon.name)
            context['detail'] = 'modificator_slug wasn`t provided.'
            return Response(context, status=status.HTTP_200_OK)

        try:
            fire_mode_slug = request.data['fire_mode_slug']
        except KeyError:
            context['message'] = Messages.ERROR['POST'](obj='WeaponDamage', name=weapon.name)
            context['detail'] = 'fire_mode_slug wasn`t provided.'
            return Response(context, status=status.HTTP_200_OK)

        modificator = get_object_or_404(Modificator, slug=modificator_slug)
        fire_mode = get_object_or_404(FireMode, slug=fire_mode_slug)

        stat_keys = ['rpm', 'dps', 'ttk']
        stat_instances = []
        for key in stat_keys:
            cur_data = request.data[key]
            cur_stat = RangeStat.objects.create(
                name=key,
                min=cur_data['min'],
                max=cur_data['max']
            )
            stat_instances.append(cur_stat)

        weapon.add_fire_mode(
            modificator=modificator,
            fire_mode=fire_mode,
            rpm=stat_instances[0],
            dps=stat_instances[1],
            ttk=stat_instances[2]
        )

        context['message'] = Messages.SUCCESS['POST'](obj='WeaponFireMode', name=weapon.name)
        context['data'] = WeaponSerializer(weapon).data
        return Response(context, status=status.HTTP_200_OK)
