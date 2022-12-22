
class RestaurantDto:
    def __init__(self, restaurant_id=''):
        self.id = restaurant_id
        self.name = ''
        self.homepage = ''
        self.lunch_source = ''
        self.city = ''
        self.crawler_id = None
        self.menus = []
