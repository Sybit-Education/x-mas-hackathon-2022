from url_registry import UrlRegistry


class DispatchFlags:
    NONE = 1 << 0
    SKIP = 1 << 0


class UrlDispatchTable(object):
    def __init__(self, registry: UrlRegistry, init_flags=DispatchFlags.NONE):
        self.table = {}
        for url in registry.get_urls():
            self.table[url] = (init_flags, url)
        self._populate()
        for k, v in self.table.items():
            assert k is not None and v is not None
            (flags, func) = v
            if (flags & DispatchFlags.SKIP) != 0:
                continue
            assert callable(func) and v.__name__ == '<lambda>'

    def _populate(self):
        pass

    def __index__(self, k):
        return self.table[k]
