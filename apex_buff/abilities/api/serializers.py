from django.db import IntegrityError
from rest_framework import serializers

from core.utils.response_messages import Context
from legends.models import Legend
from ..models import Ability


class AbilitySerializer(serializers.ModelSerializer):
    legend = serializers.CharField(source='legend.name', read_only=True)

    class Meta:
        model = Ability
        fields = [
            'slug', 'legend', 'name', 'description', 'info',
            'icon_url', 'ability_type', 'cooldown', 'icon'
        ]
        extra_kwargs = {
            'icon': {'write_only': True},
            'icon_url': {'read_only': True}
        }

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['ability_type'] = instance.get_ability_type_display()
        return rep
