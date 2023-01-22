from django.db import models
from django.contrib.auth.models import User

from .tournament_models.fighter import Fighter
# Create your models here.


class FighterModel(models.Model):
    belt_choices = (
        (0, "White"),
        (1, "Blue"),
        (2, "Purple"),
        (3, "Brown"),
        (4, "Black"),
    )
    sex_choices = (
        ("M", "Male"),
        ("F", "Female")
    )
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    belt = models.DecimalField(max_digits=1, decimal_places=1,choices=belt_choices)
    age = models.DecimalField(max_digits=3, decimal_places=1)
    sex = models.CharField(max_length=1 ,choices=sex_choices)
    uid = models.UUIDField()
    # Each Fighter model is related with a User model
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)


    def convert_to_tournament_model(self):
        fighter = Fighter(self.name, self.weight, self.belt, self.age, self.sex, self.uid)
        return fighter
    