from services.restaurant import get_all_restaurants
from os import getcwd, name as osname


class RestaurantRegistry(object):

    _restaurants = []

    def __init__(self, *opt_urls):
        """
        Initialize the registry. Loads the restaurants from service.

        Parameters:
        *opt_urls (str): Optional URL(s) to add to the registry.
        """
        restaurants = get_all_restaurants()
        self._restaurants = []
        for restaurant in restaurants:
            self._restaurants.append(restaurant)
        for i in range(len(self._restaurants)):
            print(f'Url #{i}: \'{self._restaurants[i].lunch_source}\'')
        print(f'Restaurant registry online {len(self._restaurants)} available')

    @property
    def get_restaurants(self):
        """
        Get the Restaurants in the registry.

        Returns:
        List[str]: A list of the URLs in the registry.
        """
        return self._restaurants
