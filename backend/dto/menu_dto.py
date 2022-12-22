

class MenuDto:
    def __init__(self, name, description=None, price=None):
        self.name = name
        self.description = description if description is not None else ''
        self.price = price if price is not None else ''
