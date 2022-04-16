from rest_framework import serializers

from apps.api.v1.card.models import GeneralMonster


class GeneralMonsterSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')
    subtype = serializers.CharField(source='get_subtype_display')
    rarity = serializers.CharField(source='get_rarity_display')
    race = serializers.CharField(source='get_race_display')
    attribute = serializers.CharField(source='get_attribute_display')

    class Meta:
        model = GeneralMonster
        fields = (
            'card_number',
            'serial_code',
            'name',
            'description',
            'attack',
            'defence',
            'type',
            'subtype',
            'race',
            'attribute',
            'rarity',
            'archetype',
            'edition',
            'set_name',
            'img_code',
            'amount',
        )
