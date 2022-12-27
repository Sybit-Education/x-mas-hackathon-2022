class RestaurantDto:
    def __init__(self, restaurant_id: str = ''):
        self.id = restaurant_id
        self.name = ''
        self.homepage = ''
        self.notes = ''
        self.lunch_source = ''
        self.city = ''
        self.crawler_id = None
        self.menus = []

    def __str__(self) -> str:
        return "RestaurantDTO: { id=" + self.id + ", name=" + self.name + ", crawler_id=" + self.crawler_id + "}"


