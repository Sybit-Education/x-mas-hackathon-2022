import logging
import os
from datetime import datetime
from pyairtable.formulas import match, FIND, FIELD

import pyairtable
from pyairtable import Table

from dto.menu_dto import MenuDto
from dto.restaurant_dto import RestaurantDto


def get_today_lunch():
    api_key = os.environ['AIRTABLE_API_KEY']
    base_key = os.environ['AIRTABLE_BASE_KEY']
    table = Table(api_key, base_key, "Lunch")
    lunch_list = []
    for records in table.iterate(page_size=1, max_records=1000, view="today"):
        for record in records:
            fields = record["fields"]
            menu = MenuDto(fields["Date"], fields["Name"])
            menu.description = fields["Description"] if "Description" in fields else None
            menu.price = fields["Price"]
            menu.restaurant_id = fields["Restaurant"][0]
            lunch_list.append(menu)

    return lunch_list


def add_lunch(menu_dto: MenuDto):
    logging.info("add lunch: menu: %s", menu_dto)

    api_key = os.environ['AIRTABLE_API_KEY']
    base_key = os.environ['AIRTABLE_BASE_KEY']
    table = Table(api_key, base_key, "Lunch")

    menu = {
        "Restaurant": [menu_dto.restaurant_id],
        "Name": menu_dto.name,
        "Description": menu_dto.description,
        "Price": menu_dto.price,
        "Date": pyairtable.utils.date_to_iso_str(menu_dto.date)
    }

    table.create(menu)


def delete_lunch(restaurant: RestaurantDto):
    logging.info("Delete lunch: restaurant_id=%s", restaurant)

    api_key = os.environ['AIRTABLE_API_KEY']
    base_key = os.environ['AIRTABLE_BASE_KEY']
    table = Table(api_key, base_key, "Lunch")
    formula = match({"Restaurant": restaurant.name}, match_any=True)
    records = table.all(formula=formula)
    delete_ids = []
    for record in records:
        delete_ids.append(record['id'])

    table.batch_delete(delete_ids)
