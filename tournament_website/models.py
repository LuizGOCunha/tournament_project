import uuid

from django.db import models
from django.contrib.auth.models import User

from .tournament_models.fighter import Fighter

# Create your models here.


class TournamentDjangoModel(models.Model):
    name = models.CharField(max_length=150)
    participant_limit = models.IntegerField()
    description = models.TextField(max_length=500)


class FighterDjangoModel(models.Model):
    belt_choices = (
        (0, "White"),
        (1, "Blue"),
        (2, "Purple"),
        (3, "Brown"),
        (4, "Black"),
    )
    sex_choices = (("M", "Male"), ("F", "Female"))

    # Each Fighter model should be related with a User model
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
        related_name="fighter",
    )
    name = models.CharField(max_length=150)
    # If number in database surpasses the maximum it returns a decimal.InvalidOperation Error \/
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    belt = models.IntegerField()
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=sex_choices)
    uid = models.UUIDField(
        default=uuid.uuid4(),
    )
    tournament = models.ForeignKey(
        TournamentDjangoModel,
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
        related_name="participants",
    )

    def convert_to_tournament_model(self):
        fighter = Fighter(
            self.name, self.weight, self.belt, self.age, self.sex, self.uid
        )
        return fighter
