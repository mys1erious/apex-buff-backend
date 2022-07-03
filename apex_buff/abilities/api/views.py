from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions import IsAdminOrReadOnly
from ..models import Ability
from .serializers import AbilitySerializer


class AbilityListAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, *args, **kwargs):
        abilities = Ability.objects.all()
        serializer = AbilitySerializer(abilities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = AbilitySerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AbilityDetailAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, slug, format=None):
        ability = get_object_or_404(Ability, slug=slug)
        serializer = AbilitySerializer(ability, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
