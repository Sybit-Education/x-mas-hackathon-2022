from venv import logger

import services
from dto.menu_dto import MenuDto
from restaurant_registry import RestaurantRegistry
from services import restaurant
from services.lunch import add_lunch, delete_lunch
from datetime import datetime
from pyairtable.utils import datetime_to_iso_str
from crawlers.__register__ import register_crawlers
from services.restaurant import get_all_restaurants
from crawler_mapping import CrawlerMapping

"""
A class that stores a mapping from URLs to functions and flags.
The functions in the mapping are called 'dispatch functions'.
The flags are used to control the behavior of the dispatch functions.
"""


class UrlDispatchTable(object):
    DISPATCH_TABLE = register_crawlers()
    """
    A list of dispatch functions that are used to populate the dispatch table.
    """

    def __init__(self, registry: RestaurantRegistry):
        """
        Initializes the dispatch table.

        param registry: An instance of the `RestaurantRegistry` class.
        """
        self.table = {}
        for rest in get_all_restaurants():
            if rest.crawler_id in self.DISPATCH_TABLE:
                self.table[rest.crawler_id] = CrawlerMapping(rest, self.DISPATCH_TABLE[rest.crawler_id])
            else:
                logger.warn(f'Missing crawler for id: \'{rest.crawler_id}\'')
        logger.info(f'Dispatch table online - {len(self.table)} dispatch pairs available')

    def __call__(self, *args, **kwargs) -> []:
        """
        Calls the dispatch functions in the table for each URL.

        param args: Positional arguments to be passed to the dispatch functions.
        param kwargs: Keyword arguments to be passed to the dispatch functions.
        """
        print(f'Invoking dispatch table... {len(self.table)} entries')
        ret = []
        for crawler_id, crawler_mapping in self.table.items():
            menus: list[MenuDto] = crawler_mapping.delegate(crawler_mapping.restaurant)
            # first: cleanup table for restaurant
            if len(menus) > 0:
                delete_lunch(crawler_mapping.restaurant)
            for menu in menus:
                add_lunch(menu)
            ret.append(menus)
        return ret

    def __index__(self, k):
        return self.table[k]
