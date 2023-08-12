from django.core.management.base import BaseCommand
from django.db import transaction
from tqdm import tqdm
from api.fixtures.factories import (
    CityFactory,
    UserFactory,
    RaceFactory,
    RaceTypeFactory,
    CoachFactory,
    PacerFactory,
    TrainingGroupFactory,
    PacingGroupFactory,
    UserFollowingFactory,
)


class Command(BaseCommand):
    help = "Populate the database with sample data using factories"

    from django.core.management.base import BaseCommand


from tqdm import tqdm
from api.fixtures.factories import (
    CityFactory,
    UserFactory,
    RaceFactory,
    RaceTypeFactory,
    CoachFactory,
    PacerFactory,
    TrainingGroupFactory,
    PacingGroupFactory,
    UserFollowingFactory,
)
import random


@transaction.atomic
class Command(BaseCommand):
    help = "Populate the database with sample data using factories"

    def handle(self, *args, **options):
        factories = [
            (CityFactory, {"size": 10}),
            (UserFactory, {"size": 10}),
            (CoachFactory, {"size": 10}),
            (PacerFactory, {"size": 10}),
            (TrainingGroupFactory, {"size": 10}),
            (PacingGroupFactory, {"size": 20}),
            (UserFollowingFactory, {"size": 100}),
        ]

        num_races = 50

        race_participant_ranges = (10, 50)

        for _ in tqdm(range(num_races), desc="Creating races"):
            race = RaceFactory()
            participants = random.randint(*race_participant_ranges)
            race.participants.set(UserFactory.create_batch(participants))

        num_pacers = 10
        num_pacer_race_preferences = (1, 6)
        for _ in tqdm(range(num_pacers), desc="Creating Pacers"):
            race_types = RaceTypeFactory.create_batch(
                random.randint(*num_pacer_race_preferences)
            )
            pacers = PacerFactory(distance_preferences=race_types)

        for factory_class, kwargs in tqdm(factories, desc="Creating data"):
            factory_class.create_batch(**kwargs)

        self.stdout.write(self.style.SUCCESS("Database populated with sample data"))
