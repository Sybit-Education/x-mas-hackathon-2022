from dto.restaurant_dto import RestaurantDto


class CrawlerMapping:
    def __init__(self, restaurant: RestaurantDto, delegate):
        self.restaurant = restaurant
        self.delegate = delegate
