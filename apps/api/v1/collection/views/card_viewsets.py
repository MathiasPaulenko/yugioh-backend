from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response

from apps.api.v1.collection.serializers.card_serializer import CardSerializer, DecreaseIncreaseCardSerializer
from apps.api.v1.collection import filters
from apps.api.v1.card.models import Card


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    lookup_field = "serial_code__iexact"
    lookup_value_regex = '[^/]+'
    queryset = Card.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.CardFilter
    http_method_names = ['get', 'post']


class IncreaseCardViewSet(viewsets.ModelViewSet):
    serializer_class = DecreaseIncreaseCardSerializer
    lookup_field = 'serial_code__iexact'
    queryset = Card.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        type(instance).objects.filter(pk=instance.pk).update(
            amount=F('amount') + 1,
        )

        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)


class DecreaseCardViewSet(viewsets.ModelViewSet):
    serializer_class = DecreaseIncreaseCardSerializer
    lookup_field = 'serial_code__iexact'
    queryset = Card.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        card = type(instance).objects.filter(pk=instance.pk)
        if card.first().amount > 0:
            card.update(amount=F('amount') - 1,)

        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)
