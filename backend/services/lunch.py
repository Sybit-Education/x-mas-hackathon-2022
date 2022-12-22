import os
from datetime import datetime

from pyairtable import Table

from dto.menu_dto import MenuDto


def get_today_lunch():
    api_key = os.environ['AIRTABLE_API_KEY']
    base_key = os.environ['AIRTABLE_BASE_KEY']
    table = Table(api_key, base_key, "Lunch")

    return table.all(view="today")


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
