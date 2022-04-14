from django.db import models
from rest_framework import serializers

from apps.api.v1.base.models import BaseModel
from apps.api.v1.card import choices


class Type(BaseModel):
    type = serializers.ChoiceField(choices=choices.CARD_TYPE)

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    def __str__(self):
        return self.type


class Subtype(BaseModel):
    subtype = serializers.ChoiceField(choices=choices.CARD_SUBTYPE)

    class Meta:
        verbose_name = 'Subtype'
        verbose_name_plural = 'Subtypes'

    def __str__(self):
        return self.subtype


class Race(BaseModel):
    race = serializers.ChoiceField(choices=choices.MONSTER_RACE)

    class Meta:
        verbose_name = 'Race'
        verbose_name_plural = 'Races'

    def __str__(self):
        return self.race


class Attribute(BaseModel):
    attribute = serializers.ChoiceField(choices=choices.CARD_ATTRIBUTE)

    class Meta:
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'

    def __str__(self):
        return self.attribute


class Rarity(BaseModel):
    rarity = serializers.ChoiceField(choices=choices.CARD_RARITY)

    class Meta:
        verbose_name = 'Rarity'
        verbose_name_plural = 'Rarities'

    def __str__(self):
        return self.rarity


class Card(BaseModel):
    serial_code = models.CharField('Serial Code', max_length=60, unique=True, blank=False, null=False)
    card_number = models.CharField('Card Number', max_length=60, unique=False, blank=False, null=False)
    name = models.CharField('Name', max_length=255, blank=False, null=False)
    set_name = models.CharField('Set Name', max_length=255, blank=True, null=True)
    edition = models.CharField("Edition", blank=True, max_length=80, default='')
    amount = models.IntegerField('Amount', default=0)

    rarity: Rarity = models.ForeignKey(Rarity, related_name='rarity', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    @property
    def subtype_name(self):
        return self.rarity.rarity

    def __str__(self):
        return self.name


class Monster(BaseModel):
    description = models.CharField('Description', max_length=250, blank=False, null=False)
    level = models.CharField("Level/Rank", max_length=20)
    attack = models.CharField("Attack", max_length=20)
    defence = models.CharField("Defence", max_length=20)
    archetype = models.CharField('Archetype', max_length=250, blank=True, null=True)

    subtype: Subtype = models.ForeignKey(Subtype, related_name='subtype', on_delete=models.CASCADE)
    type: Type = models.ForeignKey(Type, related_name='type', on_delete=models.CASCADE)
    race: Race = models.ForeignKey(Race, related_name='race', on_delete=models.CASCADE)
    attribute: Attribute = models.ForeignKey(Attribute, related_name='attribute', on_delete=models.CASCADE)

    @property
    def subtype_name(self):
        return self.subtype.subtype

    @property
    def type_name(self):
        return self.type.type

    @property
    def race_name(self):
        return self.race.race

    @property
    def attribute_name(self):
        return self.attribute.attribute
