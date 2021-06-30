from .views import EncoderViewSet, DecoderViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('v1/encoder', EncoderViewSet)
router.register('v2/decoder', DecoderViewSet)

