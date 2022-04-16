from rest_framework import serializers

from apps.api.v1.card.models import MagicTrapRace


class MagicTrapRaceSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_name_display')

    class Meta:
        model = MagicTrapRace
        fields = ('id', 'type')
