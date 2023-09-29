from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.db.models import OuterRef, Exists, Q
from api.models.coach import Coach
from api.models.user_following import UserFollowing
from api.models.race_registration import RaceRegistration

from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

import logging

logger = logging.getLogger(__name__)


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """

    def annotate_is_coach(self):
        return self.annotate(is_coach=Exists(Coach.objects.filter(user=OuterRef("pk"))))

    def all_visible_users_for_user(self, user):
        subquery_following = User.objects.filter(followers__user=user).values("id")

        return self.filter(
            Q(coach__isnull=False) | Q(is_private=False) | Q(id__in=subquery_following)
        )

    def create_user(self, email, password=None, **kwargs):
        password = password or kwargs.get("password")
        clerk_id = kwargs.get("clerk_id")
        if clerk_id and not password:
            password = settings.DEFAULT_CLERK_PASSWORD
        if not email:
            raise ValueError(_("Users must have an email address"))
        email = self.normalize_email(email)
        user, _ = self.model.objects.get_or_create(email=email, **kwargs)
        if password:
            user.password = password
            user.set_password(password)
            user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        """Create and save a SuperUser with the given email and password."""
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password=password, **kwargs)


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    clerk_id = models.CharField(max_length=255, unique=True, blank=True, null=True)

    home_city = models.ForeignKey(
        "City",
        related_name="city_runners",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    is_private = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def following(self):
        return User.objects.filter(followers__user=self)

    @property
    def followers(self):
        return User.objects.filter(following__following_user=self)

    def follow_user(self, user_to_follow):
        if user_to_follow.is_private:
            user_following = UserFollowing.objects.filter(
                user=self, following_user=user_to_follow
            ).first()
            if not user_following.exists():
                # send a follow request.
                pass
        else:
            user_following, created = UserFollowing.objects.get_or_create(
                following_user=user_to_follow, user=self
            )
            if created:
                logger.info(
                    f"{self.username} just requested to follow {user_to_follow.username}"
                )
        return user_following

    def unfollow_user(self, user_following):
        if usr_flwing := UserFollowing.objects.filter(
            user=self, following_user=user_following
        ).first():
            usr_flwing.delete()
            logger.info(f"{self.username} unfollowed {user_following.username}")

    def register_for_race(self, race):
        registration, created = RaceRegistration.objects.get_or_create(
            user=self, race=race
        )
        if created:
            logger.info(
                f"{self.username} just registered for {race} on {registration.registration_time}"
            )

    def unregister_from_race(self, race):
        if usr_flwing := RaceRegistration.objects.filter(user=self, race=race).first():
            usr_flwing.delete()
            logger.info(
                f"{self.username} unregistered for {race.name} at {timezone.now()}"
            )
