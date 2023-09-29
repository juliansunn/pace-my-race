from django.contrib import admin

# from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from . import models

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "password",
                    "clerk_id",
                    "email",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
    )
    ordering = ("email",)


@admin.register(models.TrainingGroup)
class TrainingGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PacingGroup)
class TrainingGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Race)
class RaceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Coach)
class CoachAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RaceType)
class RaceTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RaceRegistration)
class RaceRegistrationAdmin(admin.ModelAdmin):
    pass
