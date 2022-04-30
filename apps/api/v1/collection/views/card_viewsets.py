from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.api.v1.collection.serializers.card_serializer import CardSerializer
from apps.api.v1.card import filters
from apps.api.v1.card.models import Card


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.CardFilter
    http_method_names = ['get', ]
