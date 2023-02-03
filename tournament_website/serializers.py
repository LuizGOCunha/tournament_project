from .models import FighterDjangoModel
from rest_framework import serializers

class FighterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FighterDjangoModel
        fields = '__all__'