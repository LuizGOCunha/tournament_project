from django.contrib.auth.models import User
from rest_framework import viewsets

from .models import FighterDjangoModel
from .serializers import FighterSerializer, UserSerializer

class FighterViewset(viewsets.ModelViewSet):
    queryset = FighterDjangoModel.objects.all().order_by('id')
    serializer_class = FighterSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    