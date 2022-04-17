from rest_framework.routers import DefaultRouter

from apps.api.v1.card.api.views.attribute_viewsets import AttributeViewSet
from apps.api.v1.card.api.views.card_viewsets import CardViewSet
from apps.api.v1.card.api.views.general_monster_viewsets import GeneralMonsterViewSet
from apps.api.v1.card.api.views.link_marker_viewsets import LinkMarkerViewSet
from apps.api.v1.card.api.views.link_monster_viewsets import LinkMonsterViewSet
from apps.api.v1.card.api.views.magic_trap_card_viewsets import MagicTrapCardViewSet
from apps.api.v1.card.api.views.magictraprace_viewsets import MagicTrapRaceViewSet
from apps.api.v1.card.api.views.pendulum_monster_viewsets import PendulumMonsterViewSet
from apps.api.v1.card.api.views.rarity_viewsets import RarityViewSet
from apps.api.v1.card.api.views.subtype_viewsets import SubtypeViewSet
from apps.api.v1.card.api.views.type_viewsets import TypeViewSet

router = DefaultRouter()
router.register(r'summary', CardViewSet, basename='summary')
router.register(r'general_monster', GeneralMonsterViewSet, basename='general_monster')
router.register(r'link_monster', LinkMonsterViewSet, basename='link_monster')
router.register(r'pendulum_monster', PendulumMonsterViewSet, basename='pendulum_monster')
router.register(r'types', TypeViewSet, basename='types')
router.register(r'subtypes', SubtypeViewSet, basename='subtypes')
router.register(r'magic_trap_race', MagicTrapRaceViewSet, basename='magic_trap_race')
router.register(r'attribute', AttributeViewSet, basename='attribute')
router.register(r'rarity', RarityViewSet, basename='rarity')
router.register(r'link_marker', LinkMarkerViewSet, basename='link_marker')
router.register(r'magic_trap_card', MagicTrapCardViewSet, basename='magic_trap_card')

urlpatterns = router.urls
