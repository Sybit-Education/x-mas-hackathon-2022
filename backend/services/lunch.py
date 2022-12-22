import os
from pyairtable import Table


def get_today_lunch():
    api_key = os.environ['AIRTABLE_API_KEY']
    base_key = os.environ['AIRTABLE_BASE_KEY']
    table = Table(api_key, base_key, "Lunch")

    return table.all(view="today")
