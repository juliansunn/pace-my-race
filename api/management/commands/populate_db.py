from django.core.management.base import BaseCommand
from django.db import transaction
from tqdm import tqdm
from api.fixtures.factories import (
    CityFactory,
    UserFactory,
    RaceFactory,
    RaceTypeFactory,
    CoachFactory,
    TrainingGroupFactory,
    PacingGroupFactory,
    UserFollowingFactory,
)

from api.models import City
from api.models.coach import Coach


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
    TrainingGroupFactory,
    PacingGroupFactory,
    UserFollowingFactory,
)
import random

race_names = [
    "Spring Sprint 5K",
    "Summer Fun Run",
    "Autumn Trail Classic",
    "Winter Wonderland Half Marathon",
    "Fast and Furious 10K",
    "Charity Run for Hope",
    "Sunrise Marathon Challenge",
    "Sunset Trail Relay",
    "Hometown Heroes 5-Miler",
    "Beachfront 10-Miler",
    "Forest Frolic 5K",
    "Mountain Peak Marathon",
    "River Run Half Marathon",
    "City Lights 10-Mile Race",
    "Country Road 5K",
    "Lakeside Trail Run",
    "Desert Dash Ultra",
    "Coastal Breeze 15K",
    "Urban Jungle 10K",
    "Wilderness Explorer Marathon",
    "Twilight Trail Relay",
    "Color Run 5K",
    "Veterans Day Tribute Race",
    "Pumpkin Spice 10-Miler",
    "Holiday Hustle 5K",
    "Spring Blossom 10K",
    "Firecracker 4th of July Run",
    "Harvest Moon Half Marathon",
    "Frosty 5K Wonderland",
    "St. Patrick's Day Shamrock Shuffle",
    "Chocolate Lovers' 5-Miler",
    "Zombie Apocalypse Run",
    "Turkey Trot 10K",
    "Polar Plunge Half Marathon",
    "Superhero Sprint 5K",
    "Haunted Halloween Hustle",
    "Thanksgiving Day Gobble Wobble",
    "Summer Solstice 15K",
    "Autumn Leaves 5-Miler",
    "Jingle Bell Jog 5K",
    "New Year's Resolution Run",
    "Valentine's Day Sweetheart Shuffle",
    "Lucky Leprechaun 10K",
    "Easter Eggstravaganza 5K",
    "Memorial Day Remembrance Run",
    "Labor Day Labor of Love",
    "Christmas in July 10-Miler",
    "Midsummer Marathon",
    "Trailblazer 10K",
    "Sunset Sprint Run Down Main",
]

city_data = [
    {
        "name": "New York",
        "state": City.StateAbbreviation.NY,
        "zip_code": 10001,
        "latitude": 40.7128,
        "longitude": -74.0060,
    },
    {
        "name": "Los Angeles",
        "state": City.StateAbbreviation.CA,
        "zip_code": 90001,
        "latitude": 34.0522,
        "longitude": -118.2437,
    },
    {
        "name": "Chicago",
        "state": City.StateAbbreviation.IL,
        "zip_code": 60601,
        "latitude": 41.8781,
        "longitude": -87.6298,
    },
    {
        "name": "Houstonville",
        "state": City.StateAbbreviation.TX,
        "zip_code": 77001,
        "latitude": 29.7604,
        "longitude": -95.3698,
    },
    {
        "name": "Miami",
        "state": City.StateAbbreviation.FL,
        "zip_code": 33101,
        "latitude": 25.7617,
        "longitude": -80.1918,
    },
    {
        "name": "Philadelphia",
        "state": City.StateAbbreviation.PA,
        "zip_code": 19101,
        "latitude": 39.9526,
        "longitude": -75.1652,
    },
    {
        "name": "Dallas",
        "state": City.StateAbbreviation.TX,
        "zip_code": 75201,
        "latitude": 32.7767,
        "longitude": -96.7970,
    },
    {
        "name": "San Francisco",
        "state": City.StateAbbreviation.CA,
        "zip_code": 94101,
        "latitude": 37.7749,
        "longitude": -122.4194,
    },
    {
        "name": "Boston",
        "state": City.StateAbbreviation.MA,
        "zip_code": 10001,
        "latitude": 42.3601,
        "longitude": -71.0589,
    },
    {
        "name": "Seattle",
        "state": City.StateAbbreviation.WA,
        "zip_code": 98101,
        "latitude": 47.6062,
        "longitude": -122.3321,
    },
    {
        "name": "Denver",
        "state": City.StateAbbreviation.CO,
        "zip_code": 80201,
        "latitude": 39.7392,
        "longitude": -104.9903,
    },
    {
        "name": "Atlanta",
        "state": City.StateAbbreviation.GA,
        "zip_code": 30301,
        "latitude": 33.7490,
        "longitude": -84.3880,
    },
    {
        "name": "Las Vegas",
        "state": City.StateAbbreviation.NV,
        "zip_code": 89101,
        "latitude": 36.1699,
        "longitude": -115.1398,
    },
    {
        "name": "Portland",
        "state": City.StateAbbreviation.OR,
        "zip_code": 97201,
        "latitude": 45.5051,
        "longitude": -122.6750,
    },
    {
        "name": "Austin",
        "state": City.StateAbbreviation.TX,
        "zip_code": 73301,
        "latitude": 30.2672,
        "longitude": -97.7431,
    },
    {
        "name": "Nashville",
        "state": City.StateAbbreviation.TN,
        "zip_code": 37201,
        "latitude": 36.1627,
        "longitude": -86.7816,
    },
    {
        "name": "New Orleans",
        "state": City.StateAbbreviation.LA,
        "zip_code": 70112,
        "latitude": 29.9511,
        "longitude": -90.0715,
    },
    {
        "name": "San Diego",
        "state": City.StateAbbreviation.CA,
        "zip_code": 92101,
        "latitude": 32.7157,
        "longitude": -117.1611,
    },
    {
        "name": "Minneapolis",
        "state": City.StateAbbreviation.MN,
        "zip_code": 55401,
        "latitude": 44.9778,
        "longitude": -93.2650,
    },
    {
        "name": "Detroit",
        "state": City.StateAbbreviation.MI,
        "zip_code": 48201,
        "latitude": 42.3314,
        "longitude": -83.0458,
    },
    {
        "name": "Raleigh",
        "state": City.StateAbbreviation.NC,
        "zip_code": 27601,
        "latitude": 35.7796,
        "longitude": -78.6382,
    },
    {
        "name": "Salt Lake City",
        "state": City.StateAbbreviation.UT,
        "zip_code": 84101,
        "latitude": 40.7608,
        "longitude": -111.8910,
    },
    {
        "name": "Kansas City",
        "state": City.StateAbbreviation.MO,
        "zip_code": 64101,
        "latitude": 39.0997,
        "longitude": -94.5786,
    },
    {
        "name": "Tampa",
        "state": City.StateAbbreviation.FL,
        "zip_code": 33601,
        "latitude": 27.9506,
        "longitude": -82.4572,
    },
    {
        "name": "Pittsburgh",
        "state": City.StateAbbreviation.PA,
        "zip_code": 15201,
        "latitude": 40.4406,
        "longitude": -79.9959,
    },
    {
        "name": "San Antonio",
        "state": City.StateAbbreviation.TX,
        "zip_code": 78201,
        "latitude": 29.4241,
        "longitude": -98.4936,
    },
    {
        "name": "Columbus",
        "state": City.StateAbbreviation.OH,
        "zip_code": 43201,
        "latitude": 39.9612,
        "longitude": -82.9988,
    },
    {
        "name": "St. Louis",
        "state": City.StateAbbreviation.MO,
        "zip_code": 63101,
        "latitude": 38.6270,
        "longitude": -90.1994,
    },
    {
        "name": "Charlotte",
        "state": City.StateAbbreviation.NC,
        "zip_code": 28201,
        "latitude": 35.2271,
        "longitude": -80.8431,
    },
    {
        "name": "San Jose",
        "state": City.StateAbbreviation.CA,
        "zip_code": 95101,
        "latitude": 37.3541,
        "longitude": -121.9552,
    },
    {
        "name": "Indianapolis",
        "state": City.StateAbbreviation.IN,
        "zip_code": 46201,
        "latitude": 39.7684,
        "longitude": -86.1581,
    },
    {
        "name": "Houston",
        "state": City.StateAbbreviation.TX,
        "zip_code": 77001,
        "latitude": 29.7604,
        "longitude": -95.3698,
    },
    {
        "name": "Phoenix",
        "state": City.StateAbbreviation.AZ,
        "zip_code": 85001,
        "latitude": 33.4484,
        "longitude": -112.0740,
    },
    {
        "name": "Seattleville",
        "state": City.StateAbbreviation.WA,
        "zip_code": 98101,
        "latitude": 47.6062,
        "longitude": -122.3321,
    },
    {
        "name": "Denverland",
        "state": City.StateAbbreviation.CO,
        "zip_code": 80201,
        "latitude": 39.7392,
        "longitude": -104.9903,
    },
    {
        "name": "Atlantatown",
        "state": City.StateAbbreviation.GA,
        "zip_code": 30301,
        "latitude": 33.7490,
        "longitude": -84.3880,
    },
    {
        "name": "Los Angeles City",
        "state": City.StateAbbreviation.CA,
        "zip_code": 90001,
        "latitude": 34.0522,
        "longitude": -118.2437,
    },
    {
        "name": "San Joseville",
        "state": City.StateAbbreviation.CA,
        "zip_code": 95101,
        "latitude": 37.3541,
        "longitude": -121.9552,
    },
    {
        "name": "Indianapolisville",
        "state": City.StateAbbreviation.IN,
        "zip_code": 46201,
        "latitude": 39.7684,
        "longitude": -86.1581,
    },
    {
        "name": "Detroittown",
        "state": City.StateAbbreviation.MI,
        "zip_code": 48201,
        "latitude": 42.3314,
        "longitude": -83.0458,
    },
    {
        "name": "Raleighville",
        "state": City.StateAbbreviation.NC,
        "zip_code": 27601,
        "latitude": 35.7796,
        "longitude": -78.6382,
    },
    {
        "name": "Salt Lake Cityville",
        "state": City.StateAbbreviation.UT,
        "zip_code": 84101,
        "latitude": 40.7608,
        "longitude": -111.8910,
    },
    {
        "name": "Kansas Citytown",
        "state": City.StateAbbreviation.MO,
        "zip_code": 64101,
        "latitude": 39.0997,
        "longitude": -94.5786,
    },
    {
        "name": "Charlottetown",
        "state": City.StateAbbreviation.NC,
        "zip_code": 28201,
        "latitude": 35.2271,
        "longitude": -80.8431,
    },
    {
        "name": "Denverberg",
        "state": City.StateAbbreviation.CO,
        "zip_code": 80201,
        "latitude": 39.7392,
        "longitude": -104.9903,
    },
    {
        "name": "Atlantis",
        "state": City.StateAbbreviation.GA,
        "zip_code": 30301,
        "latitude": 33.7490,
        "longitude": -84.3880,
    },
    {
        "name": "Lost City",
        "state": City.StateAbbreviation.CA,
        "zip_code": 90001,
        "latitude": 34.0522,
        "longitude": -118.2437,
    },
    {
        "name": "San Paraiso",
        "state": City.StateAbbreviation.CA,
        "zip_code": 95101,
        "latitude": 37.3541,
        "longitude": -121.9552,
    },
    {
        "name": "Indianaville",
        "state": City.StateAbbreviation.IN,
        "zip_code": 46201,
        "latitude": 39.7684,
        "longitude": -86.1581,
    },
    {
        "name": "Detroitopolis",
        "state": City.StateAbbreviation.MI,
        "zip_code": 48201,
        "latitude": 42.3314,
        "longitude": -83.0458,
    },
    {
        "name": "Raleighton",
        "state": City.StateAbbreviation.NC,
        "zip_code": 27601,
        "latitude": 35.7796,
        "longitude": -78.6382,
    },
]


class Command(BaseCommand):
    help = "Populate the database with sample data using factories"

    @transaction.atomic
    def handle(self, *args, **options):
        ranges = (5, 20)

        for i in tqdm(range(len(race_names)), desc="Creating races"):
            city_info = city_data[i]
            city = CityFactory(
                name=city_info["name"],
                state=city_info["state"],
                zip_code=city_info["zip_code"],
                latitude=city_info["latitude"],
                longitude=city_info["longitude"],
            )
            print(f"Created {city.name}: {i}")
            race = RaceFactory(name=race_names[i], city=city)
            race.participants.set(UserFactory.create_batch(random.randint(*ranges)))
            training_group = TrainingGroupFactory(race=race)
            training_group.members.set(
                UserFactory.create_batch(random.randint(*ranges))
            )
            pacing_group = PacingGroupFactory(
                race=race,
            )
            pacing_group.pacers.set(
                CoachFactory.create_batch(
                    size=random.randint(1, 3), coach_type=Coach.CoachType.PACE
                )
            )
            pacing_group.members.set(UserFactory.create_batch(random.randint(*ranges)))
            print(f"Created {race.name} for city {city.name}: {i}")

        self.stdout.write(self.style.SUCCESS("Database populated with sample data"))
