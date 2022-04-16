from rest_framework import serializers

from apps.api.v1.card.models import Card


class CardSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')
    subtype = serializers.CharField(source='get_subtype_display')
    rarity = serializers.CharField(source='get_rarity_display')

    class Meta:
        model = Card
        fields = (
            'serial_code',
            'card_number',
            'name',
            'type',
            'subtype',
            'rarity',
            'set_name',
            'edition',
            'img_code',
            'amount',
        )
