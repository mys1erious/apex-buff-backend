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
    Modificator
#     WeaponAmmo,
#     FireMode,
#     # WeaponFiremode
#     # WeaponDamage,
)
from .serializers import (
    WeaponSerializer,
    AttachmentSerializer,
    AmmoSerializer,
    ModificatorSerializer,
#     FireModeSerializer,
#     # WeaponFiremodeSerializer
#     # WeaponDamageSerializer,
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


# class FireModeListCreateAPIView(ListCreateAPIView):
#     queryset = FireMode.objects.all()
#     permission_classes = (IsAdminOrReadOnly,)
#     serializer_class = FireModeSerializer
#     lookup_field = 'slug'
#
#
# class FireModeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = FireMode.objects.all()
#     permission_classes = (IsAdminOrReadOnly,)
#     serializer_class = FireModeSerializer
#     lookup_field = 'slug'


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
    # Add PUT, DELETE methods
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, slug, format=None):
        weapon = get_object_or_404(Weapon, slug=slug)
        serializer = WeaponSerializer(weapon, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Make Detail View?
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

        context['message'] = Messages.SUCCESS['POST'](obj='Weapon', name=weapon.name)
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

        context['message'] = Messages.SUCCESS['POST'](obj='Weapon', name=weapon.name)
        context['data'] = WeaponSerializer(weapon).data
        return Response(context, status=status.HTTP_200_OK)


class WeaponMagListAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, slug, *args, **kwargs):
        weapon = get_object_or_404(Weapon, slug=slug)
        serializer = WeaponMagSerializer(weapon.mags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug, *args, **kwargs):
        context = Context()

        weapon = get_object_or_404(Weapon, slug=slug)
        modificator = get_object_or_404(Modificator, slug=request.data['modificator_slug'])
        size = request.data['size']

        weapon.add_mag(modificator, size)

        context['message'] = Messages.SUCCESS['POST'](obj='Weapon', name=weapon.name)
        context['data'] = WeaponSerializer(weapon).data
        return Response(context, status=status.HTTP_200_OK)


# class WeaponDamageAPIView(APIView):
#     def post(self, request, slug, format=None):
#         weapon = get_object_or_404(Weapon, slug=slug)
#
#         data = request.data
#         data._mutable = True
#         data['weapon'] = slug
#         data._mutable = False
#
#         serializer = WeaponDamageSerializer(data=data, many=False)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(WeaponSerializer(weapon, many=False).data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, slug, format=None):
#         weapon = get_object_or_404(Weapon, slug=slug)
#         weapon_damage = get_object_or_404(WeaponDamage, weapon=weapon)
#
#         data = request.data
#         data._mutable = True
#         data['weapon'] = slug
#         data._mutable = False
#
#         serializer = WeaponDamageSerializer(weapon_damage, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(WeaponSerializer(weapon, many=False).data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class WeaponFiremodeListAPIView(APIView):
#     permission_classes = (IsAdminOrReadOnly,)
#
#     def get(self, request, slug, format=None):
#         weapon = get_object_or_404(Weapon, slug=slug)
#
#         weapon_firemods = []
#         for firemode in weapon.firemods:
#             weapon_firemode = get_object_or_404(WeaponFiremode, weapon=weapon, firemode=firemode)
#             weapon_firemods.append(weapon_firemode)
#         serializer = WeaponFiremodeSerializer(weapon_firemods, many=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, slug, format=None):
#         data = request.data
#         data._mutable = True
#         data['weapon_slug'] = slug
#         data._mutable = False
#         print(data)
#         serializer = WeaponFiremodeSerializer(data=data, many=False)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response(status=status.HTTP_200_OK)
#
#
# class WeaponFiremodeDetailAPIView(APIView):
#     permission_classes = (IsAdminOrReadOnly,)
#
#     def get(self, request, slug, firemode_slug, format=None):
#         weapon = get_object_or_404(Weapon, slug=slug)
#         firemode = get_object_or_404(FireMode, firemode_slug)
#
#         weapon_firemode = get_object_or_404(WeaponFiremode, weapon=weapon, firemode=firemode)
#         serializer = WeaponFiremodeSerializer(weapon_firemode, many=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
