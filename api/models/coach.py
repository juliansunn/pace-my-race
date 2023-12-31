from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    class ExpertiseChoices(models.IntegerChoices):
        NONE = 0, "None Specified"
        NOVICE = 1, "Novice"
        BEGINNER = 2, "Beginner"
        INTERMEDIATE = 3, "Intermediate"
        ADVANCED = 4, "Advanced"
        EXPERT = 5, "Expert"
        PROFESSIONAL = 6, "Professional Runner"

    class CoachType(models.TextChoices):
        PACE = "PACE", "Pacer"
        COACH = "COACH", "Coach"

    class CoachStatus(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        APPLIED = "APPLIED", "Applied"
        INACTIVE = "INACTIVE", "Inactive"

    coach_type = models.CharField(
        max_length=50, choices=CoachType.choices, default=CoachType.COACH
    )
    status = models.CharField(
        max_length=50, choices=CoachStatus.choices, default=CoachStatus.APPLIED
    )

    user = models.OneToOneField(
        "api.User", on_delete=models.CASCADE, related_name="coach"
    )
    bio = models.TextField(blank=True)
    expertise = models.SmallIntegerField(
        max_length=2,
        choices=ExpertiseChoices.choices,
        default=ExpertiseChoices.NONE,
        help_text="value to give a coaches experience for users to select against",
    )
    distance_preferences = models.ManyToManyField(
        "RaceType", related_name="preferred_coaches", default=None
    )

    def __str__(self):
        return f"{self.coach_type}: {self.user.username}"
