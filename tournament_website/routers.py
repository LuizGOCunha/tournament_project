from rest_framework import routers
from .viewsets import FighterViewset

router = routers.DefaultRouter()
router.register(r'fighters', FighterViewset, basename='fighters')