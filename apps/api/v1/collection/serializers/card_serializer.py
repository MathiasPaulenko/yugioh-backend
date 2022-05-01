from rest_framework import serializers

from apps.api.v1.card.models import Card
from apps.api.v1.collection.fixtures import get_data_from_card_type


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

    def to_representation(self, instance):
        return get_data_from_card_type(instance)


class DecreaseIncreaseCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'card_number',
            'serial_code',
            'name',
            'amount',
        )
