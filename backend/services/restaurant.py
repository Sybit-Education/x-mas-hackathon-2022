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
            restaurant.lunch_source = fields["Link_for_Lunch"]
            restaurant.homepage = fields["Homepage"]  if "Homepage" in fields else None
            restaurant.city = fields["City"] if "City" in fields else None
            restaurant.logo = fields["Logo"][0]["url"] if "Logo" in fields else None
            restaurant.crawler_id = fields["Crawler_id"] if "Crawler_id" in fields else None
            restaurant.notes = fields["Notes"] if "Notes" in fields else None

            restaurants.append(restaurant)
    return restaurants
