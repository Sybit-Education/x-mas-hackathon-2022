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
            menu.description = fields["Description"] if "Description" in fields else None
            menu.price = fields["Price"]
            menu.restaurant_id = fields["Restaurant"][0]
            lunch_list.append(menu)

    return lunch_list


def add_lunch(menu_dto: MenuDto):
    print("add lunch: restaurant_id=" + menu_dto.restaurant_id + " menu: " + menu_dto.name)

    api_key = os.environ['AIRTABLE_API_KEY']
    base_key = os.environ['AIRTABLE_BASE_KEY']
    table = Table(api_key, base_key, "Lunch")

    menu = {
        "Restaurant": menu_dto.restaurant_id,
        "Name": menu_dto.name,
        "Description": menu_dto.description,
        "Price": menu_dto.price,
        "Date": menu_dto.date
    }

    table.create(menu)


def delete_lunch(restaurant_id):
    print("Delete lunch: restaurant_id=" + restaurant_id)

    api_key = os.environ['AIRTABLE_API_KEY']
    base_key = os.environ['AIRTABLE_BASE_KEY']
    table = Table(api_key, base_key, "Lunch")

    for records in table.iterate(page_size=1, max_records=1000,
                                 formula="Restaurant='" + restaurant_id + "' "):
        delete_ids = []
        for record in records:
            delete_ids.append(record.id)

        table.batch_delete(delete_ids)
