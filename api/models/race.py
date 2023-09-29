from django.db import models
import logging
from django.db.models import Exists, OuterRef


logger = logging.getLogger(__name__)


class RaceQuerySet(models.QuerySet):
    def annotate_is_favorite(self, user):
        return self.annotate(
            is_favorite=Exists(
                models.Subquery(
                    user.favorited_races.filter(id=OuterRef("id")).values("id")
                )
            )
        )

    def annotate_favorite_count(self):
        return self.annotate(favorite_count=models.Count("favorites"))

    def annotate_participant_count(self):
        return self.annotate(participant_count=models.Count("participants"))


class Race(models.Model):
    name = models.CharField(max_length=255, default=None)
    type = models.ForeignKey(
        "RaceType", blank=True, null=True, default=None, on_delete=models.SET_NULL
    )
    link = models.URLField(null=True, blank=True, default=None)
    image = models.ImageField(null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True, default=None)
    registration_open = models.BooleanField(default=True)
    registration_deadline = models.DateTimeField(default=None)
    participants = models.ManyToManyField(
        "User",
        through="RaceRegistration",
        related_name="races_participated",
        blank=True,
    )
    race_start = models.DateTimeField()
    city = models.ForeignKey("City", null=True, blank=True, on_delete=models.SET_NULL)
    favorites = models.ManyToManyField(
        "User", related_name="favorited_races", blank=True
    )

    objects: RaceQuerySet = RaceQuerySet.as_manager()

    def __str__(self):
        return self.name

    def get_distance_display(self):
        if self.distance_unit == "km":
            return f"{self.distance} kilometers"
        elif self.distance_unit == "mi":
            return f"{self.distance} miles"
        else:
            return f"{self.distance} {self.distance_unit}"
