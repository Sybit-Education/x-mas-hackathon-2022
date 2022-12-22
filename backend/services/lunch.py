import os
from datetime import datetime

from pyairtable import Table

from dto.menu_dto import MenuDto


def get_today_lunch():
    api_key = os.environ['AIRTABLE_API_KEY']
    base_key = os.environ['AIRTABLE_BASE_KEY']
    table = Table(api_key, base_key, "Lunch")
    lunch_list = []
    for records in table.iterate(page_size=1, max_records=1000, view="today"):
        for record in records:
            fields = record["fields"]
            menu = MenuDto(fields["Date"], fields["Name"])
            menu.description = fields["Description"]
            menu.price = fields["Price"]
            menu.restaurant_id = fields["Restaurant"][0]
            lunch_list.append(menu)

    return lunch_list


def add_lunch(restaurant_id, menu_dto):
    print("add lunch: restaurant_id=" + restaurant_id + " menu: " + menu_dto)

    api_key = os.environ['AIRTABLE_API_KEY']
    base_key = os.environ['AIRTABLE_BASE_KEY']
    table = Table(api_key, base_key, "Lunch")

    menu = dict()
    menu["Restaurant"] = restaurant_id
    menu["Name"] = menu_dto.name
    menu["Description"] = menu_dto.description
    menu["Price"] = menu_dto.price

    table.create(menu)
