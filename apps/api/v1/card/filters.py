from django_filters import rest_framework as filters

from apps.api.v1.card.models import Card
from apps.api.v1.card import choices


class CardFilter(filters.FilterSet):
    type = filters.ChoiceFilter(choices=choices.CARD_TYPE)
    subtype = filters.ChoiceFilter(choices=choices.CARD_SUBTYPE)

    class Meta:
        model = Card
        fields = (
            'type',
            'card_number',
            'serial_code',
            'name',
            'subtype',
        )
