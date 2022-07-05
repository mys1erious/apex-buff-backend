import os

from rest_framework import serializers

from abilities.api.serializers import AbilitySerializer
from ..models import Legend, LegendType


class LegendTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegendType
        fields = ['name', 'icon_url']


class LegendSerializer(serializers.ModelSerializer):
    abilities = AbilitySerializer(many=True, read_only=True)
    legend_type = LegendTypeSerializer(many=False, read_only=True)

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


class LegendLegendTypeSerializer(serializers.Serializer):
    legend_type = serializers.CharField()
