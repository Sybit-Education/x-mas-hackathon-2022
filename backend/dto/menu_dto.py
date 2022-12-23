import datetime


class MenuDto:
    def __init__(self, date: datetime, name: str, description: str = None, price: str = None,
                 restaurant_id: str = None):
        self.date = date
        self.name = name
        self.description = description if description is not None else ''
        self.price = price if price is not None else ''
        self.restaurant_id = restaurant_id
