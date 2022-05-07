from apps.api.v1.card import choices
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


def get_choices_inverted(data_choices):
    return {str(y).lower(): x for x, y in dict(data_choices).items()}


def get_choice_multi_query(queryset, name, value, data_choices):
    card = get_choices_inverted(data_choices)
    try:
        query = queryset.filter(**{
            name: card[str(value).lower()],
        })
        return query
    except KeyError:
        return Card.objects.none()


def get_choice_race_query(obj, serial_code, value, data_choices):
    races = get_choices_inverted(data_choices)
    try:
        return obj.filter(serial_code=serial_code, race=int(races[(str(value).lower())]))
    except KeyError:
        return obj.none()


def get_choice_attribute_query(obj, serial_code, value, choices_data):
    attribute = {str(y).lower(): x for x, y in dict(choices_data).items()}
    try:
        return obj.filter(serial_code=serial_code, attribute=int(attribute[(str(value).lower())]))
    except KeyError:
        return obj.none()


def combine_queryset(queryset, query, serial_code):
    if query:
        queryset = queryset | Card.objects.filter(serial_code=serial_code)
    return queryset


def get_card_for_level(serial_codes, value):
    queryset = Card.objects.none()
    try:
        for serial_code in serial_codes:
            card = Card.objects.filter(serial_code=serial_code).first()

            if 'pendulum' in str(card.subtype).lower():
                query = PendulumMonster.objects.filter(serial_code=serial_code, level=value)
                queryset = combine_queryset(queryset, query, serial_code)
            elif 'link' in str(card.subtype).lower():
                query = LinkMonster.objects.filter(serial_code=serial_code, link_value=int(value))
                queryset = combine_queryset(queryset, query, serial_code)
            else:
                query = GeneralMonster.objects.filter(serial_code=serial_code, level=value)
                queryset = combine_queryset(queryset, query, serial_code)

    except (Exception,):
        return Card.objects.none()
    return queryset


def get_card_for_archetype(serial_codes, value):
    queryset = Card.objects.none()
    try:
        for serial_code in serial_codes:
            card = Card.objects.filter(serial_code=serial_code).first()
            if str(card.type).lower() in ['spell', 'trap']:
                query = MagicTrapCard.objects.filter(serial_code=serial_code, archetype__icontains=value)
                queryset = combine_queryset(queryset, query, serial_code)
            else:
                if 'pendulum' in str(card.subtype).lower():
                    query = PendulumMonster.objects.filter(serial_code=serial_code, archetype__icontains=value)
                    queryset = combine_queryset(queryset, query, serial_code)
                elif 'link' in str(card.subtype).lower():
                    query = LinkMonster.objects.filter(serial_code=serial_code, archetype__icontains=value)
                    queryset = combine_queryset(queryset, query, serial_code)
                else:
                    query = GeneralMonster.objects.filter(serial_code=serial_code, archetype__icontains=value)
                    queryset = combine_queryset(queryset, query, serial_code)

    except (Exception,):
        return Card.objects.none()
    return queryset


def get_card_for_desc(serial_codes, value):
    queryset = Card.objects.none()
    try:
        for serial_code in serial_codes:
            card = Card.objects.filter(serial_code=serial_code).first()
            if str(card.type).lower() in ['spell', 'trap']:
                query = MagicTrapCard.objects.filter(serial_code=serial_code, description__icontains=value)
                queryset = combine_queryset(queryset, query, serial_code)
            elif str(card.type).lower() == 'skill':
                query = SkillCard.objects.filter(serial_code=serial_code, description__icontains=value)
                queryset = combine_queryset(queryset, query, serial_code)
            else:
                if 'pendulum' in str(card.subtype).lower():
                    query = PendulumMonster.objects.filter(serial_code=serial_code, description__icontains=value)
                    queryset = combine_queryset(queryset, query, serial_code)
                elif 'link' in str(card.subtype).lower():
                    query = LinkMonster.objects.filter(serial_code=serial_code, description__icontains=value)
                    queryset = combine_queryset(queryset, query, serial_code)
                else:
                    query = GeneralMonster.objects.filter(serial_code=serial_code, description__icontains=value)
                    queryset = combine_queryset(queryset, query, serial_code)

    except (Exception,):
        return Card.objects.none()
    return queryset


def get_card_for_attack(serial_codes, value):
    queryset = Card.objects.none()
    try:
        for serial_code in serial_codes:
            card = Card.objects.filter(serial_code=serial_code).first()
            if 'pendulum' in str(card.subtype).lower():
                query = PendulumMonster.objects.filter(serial_code=serial_code, attack=value)
                queryset = combine_queryset(queryset, query, serial_code)
            elif 'link' in str(card.subtype).lower():
                query = LinkMonster.objects.filter(serial_code=serial_code, attack=value)
                queryset = combine_queryset(queryset, query, serial_code)
            else:
                query = GeneralMonster.objects.filter(serial_code=serial_code, attack=value)
                queryset = combine_queryset(queryset, query, serial_code)

    except (Exception,):
        return Card.objects.none()
    return queryset


def get_card_for_defence(serial_codes, value):
    queryset = Card.objects.none()
    try:
        for serial_code in serial_codes:
            card = Card.objects.filter(serial_code=serial_code).first()
            if 'pendulum' in str(card.subtype).lower():
                query = PendulumMonster.objects.filter(serial_code=serial_code, defence=value)
                queryset = combine_queryset(queryset, query, serial_code)
            else:
                query = GeneralMonster.objects.filter(serial_code=serial_code, defence=value)
                queryset = combine_queryset(queryset, query, serial_code)

    except (Exception,):
        return Card.objects.none()
    return queryset


def get_card_for_race(serial_codes, value):
    queryset = Card.objects.none()
    try:
        for serial_code in serial_codes:
            card = Card.objects.filter(serial_code=serial_code).first()
            if str(card.type).lower() in ['spell', 'trap']:
                query = get_choice_race_query(MagicTrapCard.objects, serial_code, value, choices.MAGIC_TRAP_RACE)
                queryset = combine_queryset(queryset, query, serial_code)
            elif str(card.type).lower() == 'skill':
                query = SkillCard.objects.filter(serial_code=serial_code, race__icontains=value)
                queryset = combine_queryset(queryset, query, serial_code)
            else:
                if 'pendulum' in str(card.subtype).lower():
                    query = get_choice_race_query(PendulumMonster.objects, serial_code, value, choices.MONSTER_RACE)
                    queryset = combine_queryset(queryset, query, serial_code)
                elif 'link' in str(card.subtype).lower():
                    query = get_choice_race_query(LinkMonster.objects, serial_code, value, choices.MONSTER_RACE)
                    queryset = combine_queryset(queryset, query, serial_code)
                else:
                    query = get_choice_race_query(GeneralMonster.objects, serial_code, value, choices.MONSTER_RACE)
                    queryset = combine_queryset(queryset, query, serial_code)

    except(Exception,):
        return Card.objects.none()
    return queryset


def get_card_for_attribute(serial_codes, value):
    queryset = Card.objects.none()
    try:
        for serial_code in serial_codes:
            card = Card.objects.filter(serial_code=serial_code).first()
            if 'pendulum' in str(card.subtype).lower():
                query = get_choice_attribute_query(PendulumMonster.objects, serial_code, value, choices.CARD_ATTRIBUTE)
                queryset = combine_queryset(queryset, query, serial_code)
            elif 'link' in str(card.subtype).lower():
                query = get_choice_attribute_query(LinkMonster.objects, serial_code, value, choices.CARD_ATTRIBUTE)
                queryset = combine_queryset(queryset, query, serial_code)
            else:
                query = get_choice_attribute_query(GeneralMonster.objects, serial_code, value, choices.CARD_ATTRIBUTE)
                queryset = combine_queryset(queryset, query, serial_code)

    except (Exception,):
        return Card.objects.none()
    return queryset
