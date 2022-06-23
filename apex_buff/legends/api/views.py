from django.shortcuts import get_object_or_404
from rest_framework import status

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions import IsAdminOrIsAuthenticatedReadOnly
from ..models import Legend
from .serializers import LegendSerializer


class LegendListCreateAPIView(APIView):
    # permission_classes = (IsAdminOrIsAuthenticatedReadOnly,)
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        legends = Legend.objects.all()
        serializer = LegendSerializer(legends, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = LegendSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LegendRetrieveUpdateDestroyAPIView(APIView):
    #permission_classes = (IsAdminOrIsAuthenticatedReadOnly, )
    permission_classes = (AllowAny,)

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
        return Response(context, status.HTTP_204_NO_CONTENT)


# Save with generics
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
