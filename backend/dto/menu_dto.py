

class MenuDto:
    def __init__(self, date, name, description=None, price=None, restaurant_id=None):
        self.date = date
        self.name = name
        self.description = description if description is not None else ''
        self.price = price if price is not None else ''
        self.restaurant_id = restaurant_id
