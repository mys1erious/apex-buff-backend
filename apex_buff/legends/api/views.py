from django.shortcuts import get_object_or_404
from rest_framework import status

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from abilities.models import Ability
from core.permissions import IsAdminOrReadOnly
from abilities.api.serializers import AbilitySerializer
from core.utils.response_messages import Context, Messages
from ..exceptions import TooManyAbilities

from ..models import Legend, LegendType
from .serializers import LegendSerializer, LegendTypeSerializer, LegendLegendTypeSerializer


class LegendListAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, *args, **kwargs):
        legends = Legend.all_legends()
        serializer = LegendSerializer(legends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        context = Context()

        serializer = LegendSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            context['message'] = Messages.SUCCESS['POST'](obj='Legend', name=serializer.data['name'])
            context['data'] = serializer.data
            return Response(context, status=status.HTTP_201_CREATED)

        context['message'] = Messages.ERROR['VALIDATION']
        context['errors'] = serializer.errors
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


class LegendDetailAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly, )

    def get(self, request, slug, format=None):
        legend = get_object_or_404(Legend, slug=slug)
        serializer = LegendSerializer(legend, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug, format=None):
        context = Context()
        legend = get_object_or_404(Legend, slug=slug)

        serializer = LegendSerializer(legend, data=request.data)
        if serializer.is_valid():
            serializer.save()

            context['message'] = Messages.SUCCESS['PUT'](obj='Legend', name=serializer.data['name'])
            context['data'] = serializer.data
            return Response(context, status=status.HTTP_200_OK)

        context['message'] = Messages.ERROR['PUT'](obj='Legend', name=legend.name)
        context['errors'] = serializer.errors
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        context = Context()
        legend = get_object_or_404(Legend, slug=slug)

        legend_name = legend.name

        try:
            legend.delete()
            context['message'] = Messages.SUCCESS['DELETE'](obj='Legend', name=legend_name)
            return Response(context, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            context['message'] = Messages.ERROR['DELETE'](obj='Legend', name=legend_name)
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


class LegendTypeListAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly, )

    def get(self, request, *args, **kwargs):
        legend_types = LegendType.objects.all()
        serializer = LegendTypeSerializer(legend_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        context = Context()

        serializer = LegendTypeSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()

            context['message'] = Messages.SUCCESS['POST'](obj='LegendType', name=serializer.data['name'])
            context['data'] = serializer.data
            return Response(context, status=status.HTTP_201_CREATED)

        context['message'] = Messages.ERROR['VALIDATION']
        context['errors'] = serializer.errors
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


class LegendTypeDetailAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly, )

    def get(self, request, slug, format=None):
        legend_type = get_object_or_404(LegendType, slug=slug)
        serializer = LegendTypeSerializer(legend_type, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug, format=None):
        context = Context()
        legend_type = get_object_or_404(LegendType, slug=slug)

        serializer = LegendTypeSerializer(legend_type, data=request.data)

        if serializer.is_valid():
            serializer.save()

            context['message'] = Messages.SUCCESS['PUT'](obj='LegendType', name=serializer.data['name'])
            context['data'] = serializer.data
            return Response(context, status=status.HTTP_200_OK)

        context['message'] = Messages.ERROR['PUT'](obj='LegendType', name=legend_type.name)
        context['errors'] = serializer.errors
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        context = Context()
        legend_type = get_object_or_404(LegendType, slug=slug)
        legend_type_name = legend_type.name

        try:
            legend_type.delete()
            context['message'] = Messages.SUCCESS['DELETE'](obj='LegendType', name=legend_type_name)
            return Response(context, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            context['message'] = Messages.ERROR['DELETE'](obj='LegendType', name=legend_type_name)
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


class LegendLegendTypeDetailAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly, )

    def get(self, request, slug, *args, **kwargs):
        legend = get_object_or_404(Legend, slug=slug)
        serializer = LegendTypeSerializer(legend.legend_type, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug, *args, **kwargs):
        context = Context()
        legend = get_object_or_404(Legend, slug=slug)

        serializer = LegendLegendTypeSerializer(data=request.data, many=False)
        if serializer.is_valid():
            new_legend_type = get_object_or_404(LegendType, slug=serializer.data.pop('slug'))
            legend.update_legend_type(new_legend_type)

            context['message'] = Messages.SUCCESS['PUT'](obj='Legend', name=legend.name)
            context['data'] = LegendSerializer(legend, many=False).data
            return Response(context, status=status.HTTP_200_OK)

    def delete(self, request, slug, *args, **kwargs):
        context = Context()
        legend = get_object_or_404(Legend, slug=slug)
        legend_type_name = legend.legend_type.name

        try:
            legend.delete_legend_type()
            context['message'] = Messages.SUCCESS['DELETE'](obj='LegendType', name=legend_type_name)
            return Response(context, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            context['message'] = Messages.ERROR['DELETE'](obj='LegendType', name=legend_type_name)
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


class LegendAbilityListAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, slug, *args, **kwargs):
        legend = get_object_or_404(Legend, slug=slug)
        abilities = legend.abilities
        serializer = AbilitySerializer(abilities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug, *args, **kwargs):
        context = Context()
        legend = get_object_or_404(Legend, slug=slug)

        ability_serializer = AbilitySerializer(data=request.data, many=False)

        if ability_serializer.is_valid():
            ability_serializer.save(legend=legend)
            context['message'] = Messages.SUCCESS['POST'](obj='Legend', name=legend.name)
            context['data'] = LegendSerializer(legend).data
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_200_OK)


class LegendAbilityDetailAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)
