from rest_framework import serializers

from ..models import Ability


class AbilitySerializer(serializers.ModelSerializer):
    legend = serializers.CharField()

    class Meta:
        model = Ability
        fields = [
            'slug', 'legend', 'name', 'description', 'info',
            'icon', 'ability_type', 'cooldown'
        ]

    def create(self, validated_data):
        legend_slug = validated_data.pop('legend')

        return Ability.objects.create(**validated_data)
