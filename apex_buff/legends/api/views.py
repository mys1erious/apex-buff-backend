from django.shortcuts import get_object_or_404
from rest_framework import status

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions import IsAdminOrIsAuthenticatedReadOnly
from ..models import Legend, LegendType
from .serializers import LegendSerializer, LegendTypeSerializer


class LegendListCreateAPIView(APIView):
    # permission_classes = (IsAdminOrIsAuthenticatedReadOnly,)
    permission_classes = (AllowAny, )

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


class LegendRetrieveUpdateDestroyAPIView(APIView):
    #permission_classes = (IsAdminOrIsAuthenticatedReadOnly, )
    permission_classes = (AllowAny, )

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


class LegendTypeListCreateAPIView(APIView):
    permission_classes = (IsAdminUser, )

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


class LegendTypeRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = (IsAdminUser, )

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


# With generics
# class LegendListCreateAPIView(ListCreateAPIView):
#     queryset = Legend.objects.all()
#     permission_classes = (AllowAny, )
#     serializer_class = LegendSerializer
#     lookup_field = 'slug'
#
#
# class LegendRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Legend.objects.all()
#     permission_classes = (AllowAny, )
#     serializer_class = LegendSerializer
#     lookup_field = 'slug'
