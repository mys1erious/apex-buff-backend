import os

from rest_framework import serializers

from abilities.api.serializers import AbilitySerializer
from ..models import Legend, LegendType


class LegendTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegendType
        fields = ['name', 'icon']


class LegendSerializer(serializers.ModelSerializer):
    abilities = AbilitySerializer(many=True, read_only=True)
    legend_type = LegendTypeSerializer(many=False, read_only=True)

    class Meta:
        model = Legend
        fields = [
            'name', 'icon', 'slug', 'role',
            'real_name', 'gender', 'age', 'homeworld',
            'lore', 'legend_type', 'abilities'
        ]


class LegendLegendTypeSerializer(serializers.Serializer):
    legend_type = serializers.CharField()
