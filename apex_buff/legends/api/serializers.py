import os

from rest_framework import serializers

from abilities.api.serializers import AbilitySerializer
from ..models import Legend, LegendType


class LegendTypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='get_name_display', read_only=True)

    class Meta:
        model = LegendType
        fields = ['name', 'slug', 'icon', 'icon_url']
        extra_kwargs = {
            'icon': {'write_only': True},
            'icon_url': {'read_only': True}
        }


class LegendLegendTypeSerializer(serializers.Serializer):
    slug = serializers.SlugField()


class LegendSerializer(serializers.ModelSerializer):
    abilities = AbilitySerializer(many=True, read_only=True)
    legend_type = LegendTypeSerializer(many=False, read_only=True)
    gender = serializers.CharField(source='get_gender_display', read_only=True)

    class Meta:
        model = Legend
        fields = [
            'name', 'icon_url', 'icon', 'slug', 'role',
            'real_name', 'gender', 'age', 'homeworld',
            'lore', 'legend_type', 'abilities'
        ]
        extra_kwargs = {
            'icon': {'write_only': True},
            'icon_url': {'read_only': True}
        }
