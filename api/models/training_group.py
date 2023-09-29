from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    members = models.ManyToManyField("User", related_name="training_groups", blank=True)
    private_user = models.OneToOneField(
        "User",
        blank=True,
        null=True,
        related_name="private_groups",
        on_delete=models.SET_NULL,
    )
    is_active = models.BooleanField(default=True)
    city = models.ForeignKey(
        "City",
        related_name="city_races",
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_DEFAULT,
    )
    race = models.ForeignKey(
        "Race",
        related_name="race_groups",
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_DEFAULT,
    )
    coached_by = models.ForeignKey(
        "Coach",
        null=True,
        blank=True,
        related_name="coaching_groups",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_private(self):
        return self.private_user.exists()

    def add_to_group(self, user):
        if not self.is_private:
            self.members.add(user)

    def remove_from_group(self, user):
        self.members.add(user)


class TrainingGroup(Group):
    class LevelChoices(models.IntegerChoices):
        NONE = 0, "None Specified"
        BEGINNER = 1, "Beginner"
        INTERMEDIATE = 2, "Intermediate"
        ADVANCED = 3, "Advanced"

    level = models.SmallIntegerField(
        max_length=2,
        choices=LevelChoices.choices,
        default=LevelChoices.NONE,
    )

    def __str__(self):
        return f"{self.race.name}: {self.name} Training Group"


class PacingGroup(Group):
    pace_target = models.DurationField(null=True, blank=True, default=None)
    pacers = models.ManyToManyField(
        "api.Coach",
        related_name="pacing_groups",
        limit_choices_to={"coach_type": "PACE"},
        blank=True,
    )


def __str__(self):
    return f"{self.race.name} Pacing Group"
