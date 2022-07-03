from django.shortcuts import get_object_or_404
from rest_framework import status

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions import IsAdminOrReadOnly
from abilities.api.serializers import AbilitySerializer

from ..models import Legend, LegendType
from .serializers import LegendSerializer, LegendTypeSerializer, LegendLegendTypeSerializer


class LegendListAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, *args, **kwargs):
        legends = Legend.objects.all()
        serializer = LegendSerializer(legends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = LegendSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LegendDetailAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly, )

    def get(self, request, slug, format=None):
        legend = get_object_or_404(Legend, slug=slug)
        serializer = LegendSerializer(legend, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug, format=None):
        legend = get_object_or_404(Legend, slug=slug)
        serializer = LegendSerializer(legend, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        context = {}

        legend = get_object_or_404(Legend, slug=slug)
        legend_name = legend.name
        legend.delete()

        context['message'] = f'Legend `{legend_name}` has successfully been deleted'
        return Response(context, status=status.HTTP_204_NO_CONTENT)


class LegendTypeListAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly, )

    def get(self, request, *args, **kwargs):

        legend_types = LegendType.objects.all()
        serializer = LegendTypeSerializer(legend_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = LegendTypeSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LegendTypeDetailAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly, )

    def get(self, request, slug, format=None):
        legend_type = get_object_or_404(LegendType, slug=slug)
        serializer = LegendTypeSerializer(legend_type, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug, format=None):
        legend_type = get_object_or_404(LegendType, slug=slug)
        serializer = LegendTypeSerializer(legend_type, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        legend_type = get_object_or_404(LegendType, slug=slug)
        legend_type_name = legend_type.name
        legend_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LegendLegendTypeDetailAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly, )

    def get(self, request, slug, *args, **kwargs):
        legend = get_object_or_404(Legend, slug=slug)
        legend_type_serializer = LegendTypeSerializer(legend.legend_type, many=False)
        return Response(legend_type_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug, *args, **kwargs):
        context = {}

        legend = get_object_or_404(Legend, slug=slug)
        legend_type_serializer = LegendLegendTypeSerializer(request.data, many=False)

        legend_type = legend_type_serializer.data.pop('legend_type')
        if legend_type in LegendType.Names:
            legend_type = LegendType.objects.get(name=legend_type)
            legend.legend_type = legend_type
            legend.save()

            context['message'] = f'Legend type has successfully been updated to {legend_type}'
            return Response(LegendTypeSerializer(legend.legend_type, many=False).data, status=status.HTTP_200_OK)

        context['message'] = f'Wrong legend type: {legend_type}.\n' \
                             f'Allowed legend types:\n' + \
                             ', '.join([LegendType.Names.choices[i][0] for i in range(len(LegendType.Names))])
        return Response(data=context, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, slug, *args, **kwargs):
        legend = get_object_or_404(Legend, slug=slug)
        legend.legend_type = None
        legend.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class LegendAbilityListAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, slug, *args, **kwargs):
        legend = get_object_or_404(Legend, slug=slug)
        abilities = legend.abilities.all()
        serializer = AbilitySerializer(abilities, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug, *args, **kwargs):
        context = {}

        data = request.data
        data['legend'] = slug

        serializer = AbilitySerializer(data=data, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LegendAbilityDetailAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    ...
