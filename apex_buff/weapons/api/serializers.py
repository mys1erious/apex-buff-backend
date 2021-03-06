from rest_framework import serializers

from ..models import (
    Weapon,
    Attachment,
    Ammo,
    WeaponMag,
    WeaponDamage,
    Modificator,
    RangeStat,
    FireMode,
    WeaponFireMode,
    DamageStats
)


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['slug', 'name', 'icon_url', 'icon']
        extra_kwargs = {
            'icon': {'write_only': True},
            'icon_url': {'read_only': True}
        }


class AmmoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ammo
        fields = ['slug', 'name', 'icon_url', 'icon']
        extra_kwargs = {
            'icon': {'write_only': True},
            'icon_url': {'read_only': True}
        }


class FireModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireMode
        fields = ['slug', 'name', 'icon_url', 'icon']
        extra_kwargs = {
            'icon': {'write_only': True},
            'icon_url': {'read_only': True}
        }


class ModificatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modificator
        fields = ['slug', 'name', 'icon_url', 'icon']
        extra_kwargs = {
            'icon': {'write_only': True},
            'icon_url': {'read_only': True}
        }


class RangeStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RangeStat
        fields = ['name', 'min', 'max']
        extra_kwargs = {
            'name': {'write_only': True},
            'min': {'write_only': True},
            'max': {'write_only': True}
        }


# Rework 'if rep['modificator']['name'] == instance.modificator.Names.DEFAULT.label' to be in model
#   to keep serializers more dry
class MagSerializer(serializers.ModelSerializer):
    modificator = ModificatorSerializer(many=False, read_only=True)

    class Meta:
        model = WeaponMag
        fields = ['modificator', 'size']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
            if rep['modificator']['name'] == instance.modificator.Names.DEFAULT.label:
                del rep['modificator']
        except AttributeError:
            pass
        return rep


class DamageSerializer(serializers.ModelSerializer):
    modificator = ModificatorSerializer(many=False, read_only=True)
    body = RangeStatSerializer(many=False, required=False)
    head = RangeStatSerializer(many=False, required=False)
    legs = RangeStatSerializer(many=False, required=False)

    class Meta:
        model = WeaponDamage
        fields = ['modificator', 'body', 'head', 'legs']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
            if rep['modificator']['name'] == instance.modificator.Names.DEFAULT.label:
                del rep['modificator']
            rep['body'] = instance.body.value_display()
            rep['head'] = instance.head.value_display()
            rep['legs'] = instance.legs.value_display()
        except AttributeError:
            pass
        return rep


class DamageStatsSerializer(serializers.ModelSerializer):
    modificator = ModificatorSerializer(many=False, read_only=True)
    rpm = RangeStatSerializer(many=False, required=False)
    dps = RangeStatSerializer(many=False, required=False)
    ttk = RangeStatSerializer(many=False, required=False)

    class Meta:
        model = WeaponDamage
        fields = ['modificator', 'rpm', 'dps', 'ttk']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
            if rep['modificator']['name'] == instance.modificator.Names.DEFAULT.label:
                del rep['modificator']
            rep['rpm'] = instance.rpm.value_display()
            rep['dps'] = instance.dps.value_display()
            rep['ttk'] = instance.ttk.value_display()
        except AttributeError:
            pass
        return rep


class WeaponFireModeSerializer(serializers.ModelSerializer):
    fire_mode = FireModeSerializer(many=False, read_only=True)
    stats = DamageStatsSerializer(source='damage_stats', many=False, read_only=True)

    class Meta:
        model = WeaponFireMode
        fields = ['fire_mode', 'stats']


class WeaponSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=True)
    ammo = AmmoSerializer(many=True, read_only=True)
    mags = MagSerializer(many=True, read_only=True)
    projectile_speed = RangeStatSerializer(many=False, required=False)
    damage = DamageSerializer(many=True, read_only=True)
    fire_modes = WeaponFireModeSerializer(many=True, read_only=True)

    class Meta:
        model = Weapon
        fields = [
            'slug', 'name', 'icon_url', 'icon', 'weapon_type',
            'attachments', 'ammo', 'mags', 'projectile_speed',
            'damage', 'fire_modes'
        ]
        extra_kwargs = {
            'icon': {'write_only': True},
            'icon_url': {'read_only': True}
        }

    def update(self, instance, validated_data):
        # try:  # Add 'try' for a case when 'projectile_speed' not in 'validated_data'
        projectile_speed_data = validated_data.pop('projectile_speed')
        projectile_speed = RangeStat.objects.create(**projectile_speed_data)

        instance.projectile_speed = projectile_speed
        instance.save()

        return super().update(instance, validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
            rep['projectile_speed'] = instance.projectile_speed.value_display()
        except AttributeError:
            pass
        return rep
