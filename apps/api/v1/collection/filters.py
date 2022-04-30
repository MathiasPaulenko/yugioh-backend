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

    """ especial filters """
    type = filters.CharFilter(method='type_filter')
    subtype = filters.CharFilter(method='subtype_filter')
    rarity = filters.CharFilter(method='rarity_filter')

    in_collection = filters.BooleanFilter(method='in_collection_filter')
    repeated = filters.BooleanFilter(method='repeated_filter')

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
        return get_choice_query(queryset, 'subtype', value, choices.CARD_SUBTYPE)

    @staticmethod
    def rarity_filter(queryset, name, value):
        return get_choice_query(queryset, 'rarity', value, choices.CARD_RARITY)

    @staticmethod
    def in_collection_filter(queryset, name, value):
        query = {'amount__gte': 1} if value else {'amount__lte': 0}
        return queryset.filter(**query)

    @staticmethod
    def repeated_filter(queryset, name, value):
        query = {'amount__gte': 4} if value else {'amount__gt': 0, 'amount__lte': 3}
        return queryset.filter(**query)