from django.contrib.auth.models import User
from rest_framework import serializers

from .models import FighterDjangoModel


class FighterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FighterDjangoModel
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "is_superuser",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "date_joined",
            "id",
        ]
