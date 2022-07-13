from rest_framework import serializers

from ..models import (
    Ammo,
    Attachment,
    FireMode,
    Weapon,
    WeaponDamage,
    WeaponAttachment,
    WeaponFiremode,
    DamageStats
)


class AmmoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ammo
        fields = ['slug', 'name', 'icon_url', 'icon']
        extra_kwargs = {
            'icon': {'write_only': True},
            'icon_url': {'read_only': True}
        }


class AttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachment
        fields = ['slug', 'name', 'icon_url', 'icon']
        extra_kwargs = {
            'icon': {'write_only': True},
            'icon_url': {'read_only': True}
        }


class DamageStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DamageStats
        fields = ['dps', 'ttk', 'rpm']


class FireModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireMode
        fields = ['slug', 'name', 'icon_url', 'icon']
        extra_kwargs = {
            'icon': {'write_only': True},
            'icon_url': {'read_only': True}
        }


class WeaponDamageSerializer(serializers.ModelSerializer):
    weapon = serializers.CharField(write_only=True)

    class Meta:
        model = WeaponDamage
        fields = ['weapon', 'body', 'head', 'legs']

    def create(self, validated_data):
        weapon_slug = validated_data.pop('weapon')
        weapon = Weapon.objects.get(slug=weapon_slug)

        return WeaponDamage.objects.create(**validated_data, weapon=weapon)

    def update(self, instance, validated_data):
        weapon_slug = validated_data.pop('weapon')
        weapon = Weapon.objects.get(slug=weapon_slug)

        return WeaponDamage.objects.update(**validated_data, weapon=weapon)


class WeaponFiremodeSerializer(serializers.ModelSerializer):
    firemode = FireModeSerializer(many=False, read_only=True)
    damage_stats = DamageStatsSerializer(many=False, read_only=True)

    firemode_slug = serializers.SlugField(write_only=True)
    weapon_slug = serializers.SlugField(required=False, write_only=True)

    dps = serializers.FloatField(write_only=True)
    ttk = serializers.FloatField(write_only=True)
    rpm = serializers.FloatField(write_only=True)

    class Meta:
        model = WeaponFiremode
        fields = ['firemode', 'damage_stats', 'firemode_slug', 'weapon_slug', 'dps', 'ttk', 'rpm']

    def create(self, validated_data):
        weapon_slug = validated_data.pop('weapon_slug')
        weapon = Weapon.objects.get(slug=weapon_slug)

        firemode_slug = validated_data.pop('firemode_slug')
        firemode = FireMode.objects.get(slug=firemode_slug)

        damage_stats_data = {
            'dps': validated_data.pop('dps'),
            'ttk': validated_data.pop('ttk'),
            'rpm': validated_data.pop('rpm')
        }
        damage_stats = DamageStats.objects.create(**damage_stats_data)

        return WeaponFiremode.objects.create(
            weapon=weapon,
            firemode=firemode,
            damage_stats=damage_stats
        )


class WeaponSerializer(serializers.ModelSerializer):
    damage = WeaponDamageSerializer(many=False, read_only=True)
    ammo = AmmoSerializer(many=False, read_only=True)
    attachments = AttachmentSerializer(many=True, read_only=True)
    firemods = WeaponFiremodeSerializer(many=True, read_only=True, source='weapon_firemods')

    class Meta:
        model = Weapon
        fields = [
            'slug', 'name', 'icon_url', 'icon', 'weapon_type',
            'mag_size', 'projectile_speed', 'damage', 'ammo',
            'attachments', 'firemods'
        ]
        extra_kwargs = {
            'icon': {'write_only': True},
            'icon_url': {'read_only': True}
        }


# Rework
class WeaponAmmoSerializer(serializers.Serializer):
    ammo = serializers.CharField()


class WeaponAttachmentSerializer(serializers.ModelSerializer):
    attachment = serializers.CharField()
    weapon = serializers.CharField()

    class Meta:
        model = WeaponAttachment
        fields = ['attachment', 'weapon']
        extra_kwargs = {
            'weapon': {'write_only': True}
        }

    def create(self, validated_data):
        weapon_slug = validated_data.pop('weapon')
        weapon = Weapon.objects.get(slug=weapon_slug)

        attachment_slug = validated_data.pop('attachment')
        attachment = Attachment.objects.get(slug=attachment_slug)

        return WeaponAttachment.objects.create(**validated_data, weapon=weapon, attachment=attachment)