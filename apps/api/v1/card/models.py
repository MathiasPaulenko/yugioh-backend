from django.db import models
from rest_framework import serializers

from apps.api.v1.base.models import BaseModel
from apps.api.v1.card import choices


class Type(BaseModel):
    name = models.CharField(max_length=50, choices=choices.CARD_TYPE)

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    def __str__(self):
        return f"{self.name}"


class Subtype(BaseModel):
    name = models.CharField(max_length=50, choices=choices.CARD_SUBTYPE)

    class Meta:
        verbose_name = 'Subtype'
        verbose_name_plural = 'Subtypes'

    def __str__(self):
        return f"{self.name}"


class Race(BaseModel):
    name = models.CharField(max_length=50, choices=choices.MONSTER_RACE)

    class Meta:
        verbose_name = 'Race'
        verbose_name_plural = 'Races'

    def __str__(self):
        return f"{self.name}"


class MagicTrapRace(BaseModel):
    name = models.CharField(max_length=50, choices=choices.MAGIC_TRAP_RACE)

    class Meta:
        verbose_name = 'Magic/Trap Race'
        verbose_name_plural = 'Magic/Trap Races'

    def __str__(self):
        return f"{self.name}"


class Attribute(BaseModel):
    name = models.CharField(max_length=50, choices=choices.CARD_ATTRIBUTE)

    class Meta:
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'

    def __str__(self):
        return f"{self.name}"


class Rarity(BaseModel):
    name = models.CharField(max_length=50, choices=choices.CARD_RARITY)

    class Meta:
        verbose_name = 'Rarity'
        verbose_name_plural = 'Rarities'

    def __str__(self):
        return f"{self.name}"


class LinkMarker(BaseModel):
    name = models.CharField(max_length=50, choices=choices.LINK_MARKERS, default=1)

    class Meta:
        verbose_name = 'Link Marker'
        verbose_name_plural = 'Link Markers'

    def __str__(self):
        return f"{self.name}"


class Card(BaseModel):
    serial_code = models.CharField('Serial Code', max_length=60, unique=True, blank=False, null=False)
    card_number = models.CharField('Card Number', max_length=60, unique=False, blank=False, null=False)
    name = models.CharField('Name', max_length=255, blank=False, null=False)
    set_name = models.CharField('Set Name', max_length=255, blank=True, null=True)
    edition = models.CharField("Edition", blank=True, max_length=80, default='')
    amount = models.IntegerField('Amount', default=0)
    img_code = models.CharField('Image Code', max_length=20, blank=True, null=True)

    subtype: Subtype = models.ForeignKey(Subtype, related_name='subtype', on_delete=models.CASCADE)
    type: Type = models.ForeignKey(Type, related_name='type', on_delete=models.CASCADE)
    rarity: Rarity = models.ForeignKey(Rarity, related_name='rarity', on_delete=models.CASCADE)

    @property
    def rarity_name(self):
        return self.rarity.name

    @property
    def subtype_name(self):
        return self.subtype.name

    @property
    def type_name(self):
        return self.type.name

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    def __str__(self):
        return f"{self.serial_code}"


class Monster(Card):
    description = models.CharField('Description', max_length=250, blank=False, null=False)
    level = models.CharField("Level/Rank", max_length=20)
    attack = models.CharField("Attack", max_length=20)
    archetype = models.CharField('Archetype', max_length=250, blank=True, null=True)

    race: Race = models.ForeignKey(Race, related_name='monster_race', on_delete=models.CASCADE)
    attribute: Attribute = models.ForeignKey(Attribute, related_name='attribute', on_delete=models.CASCADE)

    @property
    def race_name(self):
        return self.race.name

    @property
    def attribute_name(self):
        return self.attribute.name


class MagicTrapCard(Card):
    description = models.CharField('Description', max_length=250, blank=False, null=False)
    race: Race = models.ForeignKey(Race, related_name='magic_trap_race', on_delete=models.CASCADE)

    @property
    def race_name(self):
        return self.race.name


class GeneralMonster(Monster):
    defence = models.CharField("Defence", max_length=20)

    class Meta:
        verbose_name = 'Monster'
        verbose_name_plural = 'Monster'


class LinkMonster(Monster):
    link_value = models.IntegerField('Link Value')
    link_markers: LinkMarker = models.ManyToManyField(LinkMarker)

    class Meta:
        verbose_name = 'Link Monster'
        verbose_name_plural = 'Link Monsters'


class PendulumMonster(Monster):
    scale = models.IntegerField('Scale')

    class Meta:
        verbose_name = 'Pendulum Monster'
        verbose_name_plural = 'Pendulum Monsters'
