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
from .serializers import (
    AmmoSerializer,
    AttachmentSerializer,
    FireModeSerializer,
    WeaponSerializer,
    WeaponDamageSerializer,
    WeaponAmmoSerializer,
    WeaponAttachmentSerializer,
    WeaponFiremodeSerializer
)
from ..models import (
    Ammo,
    Attachment,
    FireMode,
    Weapon,
    WeaponDamage,
    WeaponAttachment,
    WeaponFiremode
)


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


class WeaponListAPIView(APIView):
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
    def get(self, request, slug, format=None):
        weapon = get_object_or_404(Weapon, slug=slug)
        serializer = WeaponSerializer(weapon, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WeaponDamageAPIView(APIView):
    def post(self, request, slug, format=None):
        weapon = get_object_or_404(Weapon, slug=slug)

        data = request.data
        data._mutable = True
        data['weapon'] = slug
        data._mutable = False

        serializer = WeaponDamageSerializer(data=data, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response(WeaponSerializer(weapon, many=False).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, slug, format=None):
        weapon = get_object_or_404(Weapon, slug=slug)
        weapon_damage = get_object_or_404(WeaponDamage, weapon=weapon)

        data = request.data
        data._mutable = True
        data['weapon'] = slug
        data._mutable = False

        serializer = WeaponDamageSerializer(weapon_damage, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(WeaponSerializer(weapon, many=False).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WeaponAmmoAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def put(self, request, slug, *args, **kwargs):
        context = {}

        weapon = get_object_or_404(Weapon, slug=slug)
        weapon_ammo_serializer = WeaponAmmoSerializer(request.data, many=False)

        ammo_name = weapon_ammo_serializer.data.pop('ammo')
        if ammo_name in Ammo.Names:
            ammo = Ammo.objects.get(name=ammo_name)
            weapon.ammo = ammo
            weapon.save()

            context['message'] = f'Weapon ammo has successfully been updated to {ammo_name}'
            return Response(WeaponSerializer(weapon, many=False).data, status=status.HTTP_200_OK)

        context['message'] = f'Wrong ammo type: {ammo_name}.\n' \
                             f'Allowed ammo types:\n' + \
                             ', '.join([Ammo.Names.choices[i][0] for i in range(len(Ammo.Names))])
        return Response(data=context, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, slug, *args, **kwargs):
        weapon = get_object_or_404(Weapon, slug=slug)
        weapon.ammo.delete()
        weapon.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WeaponAttachmentAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, slug, format=None):
        weapon = get_object_or_404(Weapon, slug=slug)
        print(weapon.attachments)
        serializer = AttachmentSerializer(weapon.attachments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug, format=None):
        data = request.data
        data._mutable = True
        data['weapon'] = slug
        data._mutable = False

        serializer = WeaponAttachmentSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WeaponFiremodeListAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, slug, format=None):
        weapon = get_object_or_404(Weapon, slug=slug)

        weapon_firemods = []
        for firemode in weapon.firemods:
            weapon_firemode = get_object_or_404(WeaponFiremode, weapon=weapon, firemode=firemode)
            weapon_firemods.append(weapon_firemode)
        serializer = WeaponFiremodeSerializer(weapon_firemods, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug, format=None):
        data = request.data
        data._mutable = True
        data['weapon_slug'] = slug
        data._mutable = False
        print(data)
        serializer = WeaponFiremodeSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)


class WeaponFiremodeDetailAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, slug, firemode_slug, format=None):
        weapon = get_object_or_404(Weapon, slug=slug)
        firemode = get_object_or_404(FireMode, firemode_slug)

        weapon_firemode = get_object_or_404(WeaponFiremode, weapon=weapon, firemode=firemode)
        serializer = WeaponFiremodeSerializer(weapon_firemode, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
