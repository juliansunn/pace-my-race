from django.db import models
from api.models.coach import Coach


class Pacer(Coach):
    distance_preferences = models.ManyToManyField(
        "RaceType", related_name="type_pacers", default=None
    )

    def __str__(self):
        return self.user.username
