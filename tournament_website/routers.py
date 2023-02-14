from rest_framework import routers
from .viewsets import FighterViewset, UserViewset

router = routers.DefaultRouter()
router.register(r"fighters", FighterViewset, basename="fighters")
router.register(r"users", UserViewset, basename="users")
