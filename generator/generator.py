import random

from data.data import Person, Date
from faker import Faker

faker_ru = Faker("ru_RU")
faker = Faker("EN")
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        age=random.randint(18, 99),
        salary=random.randint(1000, 9999),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        department=faker_ru.job(),
        mobile=faker_ru.msisdn()
    )

def generated_date():
    yield Date(
        date=faker.day_of_month(),
        month=faker.month_name(),
        year=faker.year(),
        time="14:00"
    )