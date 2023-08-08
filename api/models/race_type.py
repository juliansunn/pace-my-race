from django.db import models


class RaceType(models.Model):
    class RaceChoices(models.IntegerChoices):
        KM = 0, "Kilometers"
        MI = 1, "Miles"

    class SurfaceChoices(models.IntegerChoices):
        NONE_SPECIFIED = 0, "Not Specified"
        ROAD = 1, "Road"
        TRAIL = 2, "Trail"
        ROAD_TRAIL = 3, "Road/Trail"
        TRACK = 4, "Track"

    distance = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    surface = models.SmallIntegerField(
        max_length=2,
        choices=SurfaceChoices.choices,
        default=SurfaceChoices.NONE_SPECIFIED,
    )

    description = models.TextField()
    distance_unit = models.SmallIntegerField(
        max_length=2, choices=RaceChoices.choices, default=RaceChoices.KM
    )

    def __str__(self):
        return f"{self.distance} {self.distance_unit} - {self.description}"
