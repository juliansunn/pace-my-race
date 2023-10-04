from django.contrib import admin

# from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from . import models
from api.models import Coach

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


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    actions = ["set_coaches_active", "set_coaches_inactive"]

    def set_coaches_active(self, request, queryset):
        queryset.update(status=Coach.CoachStatus.ACTIVE)

    set_coaches_active.short_description = "Set selected coaches to Active"

    def set_coaches_inactive(self, request, queryset):
        queryset.update(status=Coach.CoachStatus.INACTIVE)

    set_coaches_inactive.short_description = "Set selected coaches to Inactive"


@admin.register(models.RaceType)
class RaceTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RaceRegistration)
class RaceRegistrationAdmin(admin.ModelAdmin):
    pass
