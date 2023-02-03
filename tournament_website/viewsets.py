from rest_framework import viewsets

from .models import FighterDjangoModel
from .serializers import FighterSerializer

class FighterViewset(viewsets.ModelViewSet):
    queryset = FighterDjangoModel.objects.all().order_by('id')
    serializer_class = FighterSerializer
    