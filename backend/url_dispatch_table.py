from crawlers import la_olivia
from dto.restaurant_dto import RestaurantDto
from url_registry import UrlRegistry
from services.lunch import add_lunch
from services.restaurant import get_all_restaurants

"""
A class that stores a mapping from URLs to functions and flags.
The functions in the mapping are called 'dispatch functions'.
The flags are used to control the behavior of the dispatch functions.
"""


class DispatchFlags:
    NONE = 0 << 0
    SKIP = 1 << 0


class UrlDispatchTable(object):
    class UrlMapping:
        def __init__(self, id: str, delegate, url: str, flags: int = DispatchFlags.NONE):
            self.id = id
            self.delegate = delegate
            self.url = url
            self.flags = flags

    DISPATCH_TABLE = {
        'la_oliva': lambda url: la_olivia.LaOliviaCrawler().crawl(url),
    }
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
                self.table[url.id] = self.UrlMapping(url.id, self.DISPATCH_TABLE[url.id], url.url)
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
        for k, v in self.table.items():
            if (v.flags & DispatchFlags.SKIP) != 0:
                continue
            r: RestaurantDto = v.delegate(v.url)
            rid = None
            for r in get_all_restaurants():
                if r.crawler_id == v.id:
                    rid = r.id
                    break
            for m in r.menus:
                add_lunch(rid, m)
            ret.append(r)
        return ret

    def __index__(self, k):
        return self.table[k]
