from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    class ExpertiseChoices(models.IntegerChoices):
        NONE = 0, "None Specified"
        NOVICE = 1, "None Specified"
        BEGINNER = 2, "Beginner"
        INTERMEDIATE = 3, "Intermediate"
        ADVANCED = 4, "Advanced"
        EXPERT = 5, "Expert"
        PROFESSIONAL = 6, "Professional Runner"

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
    # Other fields relevant to a coach's information

    def __str__(self):
        return self.user.username
