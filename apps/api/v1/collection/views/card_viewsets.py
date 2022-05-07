from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.v1.collection.serializers.card_serializer import (
    CardSerializer,
    DecreaseIncreaseCardSerializer,
    CreateGeneralMonsterSerializer,
    CreateSkillCardSerializer,
    CreateMagicTrapCardSerializer,
    CreatePendulumMonsterSerializer,
    CreateLinkMonsterSerializer
)
from apps.api.v1.collection import filters, responses
from apps.api.v1.card.models import Card, GeneralMonster, LinkMonster, PendulumMonster, MagicTrapCard, SkillCard
from apps.api.v1.card import choices


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    lookup_field = "serial_code__iexact"
    lookup_value_regex = '[^/]+'
    queryset = Card.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.CardFilter
    http_method_names = ['get', 'post', 'delete']


class CreateUpdateCardViewSet(APIView):
    lookup_field = "serial_code__iexact"
    lookup_value_regex = '[^/]+'
    http_method_names = ['post', 'put']

    @staticmethod
    def post(request):
        try:
            card_type = request.data['type']
            if str(card_type).lower() == '4':
                serializer = CreateSkillCardSerializer(data=request.data)
            elif str(card_type).lower() in ['2', '3']:
                serializer = CreateMagicTrapCardSerializer(data=request.data)
            elif str(card_type).lower() in ['1', '5']:
                subtype_choices = dict(choices.CARD_SUBTYPE)
                card_subtype = subtype_choices[str(request.data['subtype'])]
                if 'pendulum' in str(card_subtype).lower():
                    serializer = CreatePendulumMonsterSerializer(data=request.data)
                elif 'link' in str(card_subtype).lower():
                    serializer = CreateLinkMonsterSerializer(data=request.data)
                else:
                    serializer = CreateGeneralMonsterSerializer(data=request.data)

            else:
                return responses.INVALID_TYPE
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        except (Exception,) as ex:
            print(ex)
            return responses.GENERAL_ERROR

    @staticmethod
    def put(request, serial_code):
        try:
            if serial_code != request.data['serial_code']:
                return Response(status=status.HTTP_409_CONFLICT)
            card = Card.objects.get(serial_code=serial_code)
            card_type = card.type
            if str(card_type).lower() == 'skill':
                card = SkillCard.objects.get(serial_code=serial_code)
                serializer = CreateSkillCardSerializer(card, data=request.data, partial=True)
            elif str(card_type).lower() in ['trap', 'spell']:
                card = MagicTrapCard.objects.get(serial_code=serial_code)
                serializer = CreateMagicTrapCardSerializer(card, data=request.data, partial=True)
            elif str(card_type).lower() in ['monster', 'token']:
                card_subtype = card.subtype
                if 'pendulum' in str(card_subtype).lower():
                    pendulum_monster = PendulumMonster.objects.get(serial_code=serial_code)
                    serializer = CreatePendulumMonsterSerializer(pendulum_monster, data=request.data, partial=True)
                elif 'link' in str(card_subtype).lower():
                    link_monster = LinkMonster.objects.get(serial_code=serial_code)
                    serializer = CreateLinkMonsterSerializer(link_monster, data=request.data, partial=True)
                else:
                    monster = GeneralMonster.objects.get(serial_code=serial_code)
                    serializer = CreateGeneralMonsterSerializer(monster, data=request.data, partial=True)
            else:
                return responses.INVALID_TYPE

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        except (Exception,) as ex:
            print(ex)
            return responses.GENERAL_ERROR


class IncreaseCardViewSet(viewsets.ModelViewSet):
    serializer_class = DecreaseIncreaseCardSerializer
    lookup_field = 'serial_code__iexact'
    queryset = Card.objects.all()
    http_method_names = ['get', ]

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
    http_method_names = ['get', ]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        card = type(instance).objects.filter(pk=instance.pk)
        if card.first().amount > 0:
            card.update(amount=F('amount') - 1, )

        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)
