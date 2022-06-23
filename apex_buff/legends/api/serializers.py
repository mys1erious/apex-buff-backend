from rest_framework import serializers

from ..models import Legend, LegendType


class LegendTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegendType
        fields = ['name', 'icon']


class LegendSerializer(serializers.ModelSerializer):
    abilities = serializers.CharField(default='', read_only=True)  # For now
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
