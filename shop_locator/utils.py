import random

from faker import Faker
from drf_yasg import openapi


def fill_db_cities_streets(city_model, street_model):
    faker = Faker('ru_RU')
    city_names = set()
    street_names = set()

    while len(city_names) <= 4:
        city_names.add(faker.city_name())

    while len(street_names) <= 8:
        street_names.add(faker.street_title())

    streets = []
    for city_name in city_names:
        city = city_model.objects.create(name=city_name)

        for street_name in random.sample(list(street_names), k=4):
            streets.append(street_model(name=street_name, city=city))

    street_model.objects.bulk_create(streets)


# custom properties for ShopListCreateView
PROPERTIES = {
    'name': openapi.Schema(
        type=openapi.TYPE_STRING,
        default='Shop',
    ),
    'city': openapi.Schema(
        type=openapi.TYPE_INTEGER,
        default=1,
    ),
    'street': openapi.Schema(
        type=openapi.TYPE_INTEGER,
        default=1,
    ),
    'house': openapi.Schema(
        type=openapi.TYPE_INTEGER,
        default=10,
    ),
    'opening_time': openapi.Schema(
        type=openapi.TYPE_STRING,
        default='10:00:00',
    ),
    'closing_time': openapi.Schema(
        type=openapi.TYPE_STRING,
        default='18:00:00',
    ),
}
