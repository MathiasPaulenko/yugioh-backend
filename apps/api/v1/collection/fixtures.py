from apps.api.v1.card.models import (
    MagicTrapCard,
    GeneralMonster,
    LinkMonster,
    PendulumMonster,
    SkillCard,
    Card
)
from apps.api.v1.card.api.serializers.general_monster_serializer import GeneralMonsterSerializer
from apps.api.v1.card.api.serializers.link_monster_serializer import LinkMonsterSerializer
from apps.api.v1.card.api.serializers.magic_trap_card_serializer import MagicTrapCardSerializer
from apps.api.v1.card.api.serializers.pendulum_monster_serializer import PendulumMonsterSerializer
from apps.api.v1.card.api.serializers.skill_serializer import SkillCardSerializer


def get_data_from_card_type(instance):
    card_type = instance.type
    card_serial_code = instance.serial_code
    if str(card_type).lower() == 'skill':
        card_filter = SkillCard.objects.filter(serial_code=card_serial_code).first()
        return SkillCardSerializer(card_filter).data
    elif str(card_type).lower() in ['spell', 'trap']:
        card_filter = MagicTrapCard.objects.filter(serial_code=card_serial_code).first()
        return MagicTrapCardSerializer(card_filter).data
    else:
        card_subtype = instance.subtype
        if 'pendulum' in str(card_subtype).lower():
            card_filter = PendulumMonster.objects.filter(serial_code=card_serial_code).first()
            return PendulumMonsterSerializer(card_filter).data
        elif 'link' in str(card_subtype).lower():
            card_filter = LinkMonster.objects.filter(serial_code=card_serial_code).first()
            return LinkMonsterSerializer(card_filter).data
        else:
            card_filter = GeneralMonster.objects.filter(serial_code=card_serial_code).first()
            return GeneralMonsterSerializer(card_filter).data


def get_choice_query(queryset, name, value, data_choices):
    card = {str(y).lower(): x for x, y in dict(data_choices).items()}

    try:
        query = queryset.filter(**{
            name: card[str(value).lower()],
        })
        return query
    except KeyError:
        return Card.objects.none()