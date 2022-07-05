from rest_framework import serializers

from legends.models import Legend
from ..models import Ability


class AbilitySerializer(serializers.ModelSerializer):
    legend = serializers.CharField()

    class Meta:
        model = Ability
        fields = [
            'slug', 'legend', 'name', 'description', 'info',
            'icon_url', 'icon', 'ability_type', 'cooldown'
        ]
        extra_kwargs = {
            'icon': {'write_only': True},
            'icon_url': {'read_only': True}
        }

    def create(self, validated_data):
        legend_slug = validated_data.pop('legend')
        legend = Legend.objects.get(slug=legend_slug)

        return Ability.objects.create(**validated_data, legend=legend)
