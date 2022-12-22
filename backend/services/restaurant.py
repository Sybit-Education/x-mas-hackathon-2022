import os
from pyairtable import Table

from dto.restaurant_dto import RestaurantDto


def get_all_restaurants():
    api_key = os.environ['AIRTABLE_API_KEY']
    base_key = os.environ['AIRTABLE_BASE_KEY']
    table = Table(api_key, base_key, "Restaurant")
    restaurants = []
    for records in table.iterate(page_size=1, max_records=1000, view="public"):
        for record in records:
            print(record)
            fields = record["fields"]
            restaurant = RestaurantDto(record['id'])
            restaurant.name = fields["Name"]
            restaurant.homepage = fields["Homepage"]
            restaurant.lunch_source = fields["Link_Mittagstisch"]

            restaurants.append(restaurant)
    return restaurants
