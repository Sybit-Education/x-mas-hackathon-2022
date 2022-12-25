from dto.menu_dto import MenuDto
from url_registry import UrlRegistry
from services.lunch import add_lunch
from datetime import datetime
from pyairtable.utils import datetime_to_iso_str
from crawlers.__register__ import register_crawlers
from url_mapping import UrlMapping, DispatchFlags

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

    def __init__(self, registry: UrlRegistry, init_flags=DispatchFlags.NONE):
        """
        Initializes the dispatch table.

        param registry: An instance of the `UrlRegistry` class.
        param init_flags: An integer representing the initial flags for each dispatch function in the table.
        """
        self.table = {}
        i = 0
        for url in registry.get_urls:
            if url.id in self.DISPATCH_TABLE:
                self.table[url.id] = UrlMapping(url.id, self.DISPATCH_TABLE[url.id], url.url)
                i += i
            else:
                print(f'Missing crawler for id: \'{url.id}\'')
        print(f'Dispatch table online - {i} dispatch pairs available')

    def __call__(self, *args, **kwargs) -> []:
        """
        Calls the dispatch functions in the table for each URL.

        param args: Positional arguments to be passed to the dispatch functions.
        param kwargs: Keyword arguments to be passed to the dispatch functions.
        """
        print(f'Invoking dispatch table... {len(self.table)} entries')
        ret = []
        for key, value in self.table.items():
            if (value.flags & DispatchFlags.SKIP) != 0:
                continue
            menus: list[MenuDto] = value.delegate(value)
            for menu in menus:
                menu.date = datetime_to_iso_str(datetime.now())
                add_lunch(menu)
            ret.append(menus)
        return ret

    def __index__(self, k):
        return self.table[k]
