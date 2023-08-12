import factory
from api.models import (
    User,
    Race,
    City,
    Coach,
    Pacer,
    RaceRegistration,
    RaceType,
    Group,
    TrainingGroup,
    PacingGroup,
    UserFollowing,
)

from datetime import datetime, timedelta
from django.utils import timezone

from .providers import Provider


factory.Faker.add_provider(Provider)


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    state = factory.Faker(
        "random_element", elements=[abbr for abbr, _ in City.StateAbbreviation.choices]
    )
    name = factory.Faker("unique_word")
    latitude = factory.Faker("latitude")
    longitude = factory.Faker("longitude")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username", "clerk_id")

    email = factory.Faker("unique_email")
    username = factory.Faker("unique_username")
    clerk_id = factory.Faker("uuid4")  # Generate a UUID as the clerk_id
    home_city = factory.SubFactory(CityFactory)
    is_private = False  # Set the default value to False


class UserFollowingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserFollowing

    user = factory.SubFactory(UserFactory)
    following_user = factory.SubFactory(UserFactory)


class CoachFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Coach

    user = factory.SubFactory(UserFactory)
    bio = factory.Faker("paragraph")
    expertise = factory.Faker(
        "random_element",
        elements=[choice[0] for choice in Coach.ExpertiseChoices.choices],
    )


class RaceTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RaceType

    distance = factory.Faker("pydecimal", left_digits=2, right_digits=2, positive=True)
    surface = factory.Faker(
        "random_element",
        elements=[choice[0] for choice in RaceType.SurfaceChoices.choices],
    )
    description = factory.Faker("paragraph")
    distance_unit = factory.Faker(
        "random_element",
        elements=[choice[0] for choice in RaceType.RaceChoices.choices],
    )


class PacerFactory(CoachFactory):
    class Meta:
        model = Pacer

    @factory.post_generation
    def distance_preferences(self, create, extracted, **kwargs):
        if not create:
            # Only handle the post-generation logic if creating an instance
            return

        if extracted:
            if isinstance(extracted, (list, tuple)):
                # If extracted is a list or tuple of RaceType instances, add them
                self.distance_preferences.add(*extracted)
            else:
                # If extracted is a single RaceType instance, add it
                self.distance_preferences.add(extracted)


class RaceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Race

    name = factory.Faker(
        "sentence", nb_words=4
    )  # Generate a random sentence as the name
    type = factory.SubFactory(RaceTypeFactory)  # Assuming you have a RaceTypeFactory
    link = factory.Faker("url")
    description = factory.Faker("paragraph")
    registration_open = True  # Default value is True
    registration_deadline = factory.Faker("utc_datetime", days=40)
    # Future datetime within 30 days
    race_start = factory.Faker("utc_datetime", days=60)
    # Future datetime within 60 days
    city = factory.SubFactory(CityFactory)  # Assuming you have a CityFactory

    @factory.post_generation
    def participants(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            if isinstance(extracted, int):
                users = User.objects.order_by("?")[:extracted]
            else:
                users = extracted
            for user in users:
                RaceRegistration.objects.create(user=user, race=self)


class RaceRegistrationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RaceRegistration

    user = factory.SubFactory(UserFactory)
    race = factory.SubFactory(RaceFactory)
    six_months_ago = datetime.now() - timedelta(days=180)
    registration_time = factory.Faker(
        "date_time_between", start_date=six_months_ago, end_date="now"
    )


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Faker("sentence", nb_words=4)
    is_active = True
    city = factory.SubFactory(CityFactory)
    race = factory.SubFactory(RaceFactory)
    coached_by = factory.SubFactory(CoachFactory)


class TrainingGroupFactory(GroupFactory):
    class Meta:
        model = TrainingGroup

    level = factory.Faker(
        "random_element",
        elements=[choice[0] for choice in TrainingGroup.LevelChoices.choices],
    )


class PacingGroupFactory(GroupFactory):
    class Meta:
        model = PacingGroup

    pace_target = factory.Faker("time_delta")
