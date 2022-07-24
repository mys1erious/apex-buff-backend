import time

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions import IsAdminOrReadOnly
from core.utils.response_messages import Messages, Context
from ..models import Ability
from .serializers import AbilitySerializer


class AbilityListAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, *args, **kwargs):
        abilities = Ability.all_abilities()
        serializer = AbilitySerializer(abilities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AbilityDetailAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, slug, format=None):
        ability = get_object_or_404(Ability, slug=slug)
        serializer = AbilitySerializer(ability, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug, format=None):
        context = Context()
        ability = get_object_or_404(Ability, slug=slug)

        serializer = AbilitySerializer(ability, data=request.data)
        if serializer.is_valid():
            serializer.save()

            context['message'] = Messages.SUCCESS['PUT'](obj='Ability', name=serializer.data['name'])
            context['data'] = serializer.data
            return Response(context, status=status.HTTP_200_OK)

        context['message'] = Messages.ERROR['PUT'](obj='Ability', name=ability.name)
        context['errors'] = serializer.errors
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        context = Context()
        ability = get_object_or_404(Ability, slug=slug)

        ability_name = ability.name
        try:
            ability.delete()
            context['message'] = Messages.SUCCESS['DELETE'](obj='Ability', name=ability_name)
            return Response(context, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            context['message'] = Messages.ERROR['DELETE'](obj='Ability', name=ability_name)
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
