from crawlers import la_olivia
from url_registry import UrlRegistry

"""
A class that stores a mapping from URLs to functions and flags.
The functions in the mapping are called 'dispatch functions'.
The flags are used to control the behavior of the dispatch functions.
"""


class DispatchFlags:
    NONE = 0 << 0
    SKIP = 1 << 0


class UrlDispatchTable(object):
    DISPATCH_TABLE = [
        lambda url: la_olivia.LaOliviaCrawler().crawl(url),
    ]
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
        for url in registry.get_urls:
            self.table[url] = (init_flags, None)
        self._populate()
        i: int = 0
        for k, v in self.table.items():
            assert k is not None and v is not None
            (flags, func) = v
            if (flags & DispatchFlags.SKIP) != 0:
                continue
            i += 1
            assert func is not None and callable(func) and func.__name__ == '<lambda>'
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
            (flags, func) = v
            r = func(k)
            if r is not None:
                ret.append(r)
            else:
                print(f'Failed to crawl url: \'{k}\'')
        return ret

    def _populate(self):
        """
        Populates the dispatch table with the dispatch functions from `DISPATCH_TABLE`.
        """
        for i in range(len(self.DISPATCH_TABLE)):
            self._lookup(i, self.DISPATCH_TABLE[i])

    def _lookup(self, n, f):
        """
        Looks up the dispatch function at the given index in the dispatch table and assigns it the given function.

        param n: The index of the dispatch function in the dispatch table.
        param f: The function to be assigned to the dispatch function at the given index.
        """
        assert n >= 0 and (n & ~0xFF_FF_FF_FF) == 0
        if n < 0:
            n += len(self.table)
        for i, key in enumerate(self.table):
            if i == n:
                ll = list(self.table[key])
                ll[1] = f
                self.table[key] = tuple(ll)
                return
        raise IndexError("dictionary index out of range")

    def __index__(self, k):
        return self.table[k]
