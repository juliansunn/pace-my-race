from faker.providers import BaseProvider
from random_word import RandomWords
import faker
import string
import random
from datetime import timedelta
from django.utils import timezone

faker = faker.Faker()


class Provider(BaseProvider):
    def __init__(self, generator):
        super().__init__(generator)
        self.r = RandomWords()

    def unique_word(self):
        return self.r.get_random_word()

    def unique_username(self):
        username = faker.user_name()
        suffix = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
        return f"{username}_{suffix}"

    def utc_datetime(self, **kwargs):
        dt = timezone.now()
        if days := kwargs.get("days"):
            dt += timedelta(days=random.randint(0, days))
        return dt

    def unique_email(self):
        username = self.unique_username()
        return f"{username}@fakemail.com"
