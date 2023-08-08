from django.db import models
import logging

logger = logging.getLogger(__name__)


class Race(models.Model):
    name = models.CharField(max_length=255, default=None)
    type = models.ForeignKey(
        "RaceType", blank=True, null=True, default=None, on_delete=models.SET_NULL
    )
    description = models.TextField(null=True, blank=True, default=None)
    registration_open = models.BooleanField(default=True)
    registration_deadline = models.DateTimeField(default=None)
    participants = models.ManyToManyField(
        "User", through="RaceRegistration", related_name="races_participated"
    )
    race_start = models.DateTimeField()
    city = models.ForeignKey("City", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_distance_display(self):
        if self.distance_unit == "km":
            return f"{self.distance} kilometers"
        elif self.distance_unit == "mi":
            return f"{self.distance} miles"
        else:
            return f"{self.distance} {self.distance_unit}"  # Fallback if unit is not recognized
