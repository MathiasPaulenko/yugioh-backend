from rest_framework.routers import DefaultRouter

from apps.api.v1.collection.views.card_viewsets import CardViewSet

router = DefaultRouter()
router.register(r'card', CardViewSet, basename='card')

urlpatterns = router.urls
