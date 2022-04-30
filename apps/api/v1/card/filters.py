from django_filters import rest_framework as filters

from apps.api.v1.card.models import Card
from apps.api.v1.card import choices
from apps.api.v1.collection.fixtures import get_choice_query


class CardFilter(filters.FilterSet):
    serial_code = filters.CharFilter(lookup_expr='icontains')
    card_number = filters.CharFilter(lookup_expr='icontains')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    amount = filters.NumberFilter()
    lamount = filters.NumberFilter(field_name='amount', lookup_expr='lt')
    gamount = filters.NumberFilter(field_name='amount', lookup_expr='gt')

    type = filters.CharFilter(method='type_filter')
    subtype = filters.CharFilter(method='subtype_filter')
    rarity = filters.CharFilter(method='rarity_filter')

    """ especial filters """
    level = filters.CharFilter(method='level_filter')

    class Meta:
        model = Card

        fields = (
            'type',
            'subtype',
            'name',
            'serial_code',
            'card_number',
            'rarity',
            'amount',
        )

    @staticmethod
    def type_filter(queryset, name, value):
        return get_choice_query(queryset, 'type', value, choices.CARD_TYPE)

    @staticmethod
    def subtype_filter(queryset, name, value):
        card_types = {str(y).lower(): x for x, y in dict(choices.CARD_SUBTYPE).items()}

        try:
            query = queryset.filter(**{
                'subtype': card_types[str(value).lower()],
            })
            return query
        except KeyError:
            return Card.objects.none()

    @staticmethod
    def rarity_filter(queryset, name, value):
        card_types = {str(y).lower(): x for x, y in dict(choices.CARD_RARITY).items()}

        try:
            query = queryset.filter(**{
                'rarity': card_types[str(value).lower()],
            })
            return query
        except KeyError:
            return Card.objects.none()



