from url_registry import UrlRegistry


class DispatchFlags:
    NONE = 0 << 0
    SKIP = 1 << 0


class UrlDispatchTable(object):
    DISPATCH_TABLE = [
        lambda x: x,
        lambda x: x,
        lambda x: x,
        lambda x: x,
        lambda x: x,
        lambda x: x,
        lambda x: x,
        lambda x: x,
        lambda x: x,
        lambda x: x,
        lambda x: x
    ]

    def __init__(self, registry: UrlRegistry, init_flags=DispatchFlags.NONE):
        self.table = {}
        assert len(self.DISPATCH_TABLE) == len(registry.get_urls), 'Dispatch table length is different from url registry length'
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

    def __call__(self, *args, **kwargs):
        print(f'Invoking dispatch table... {len(self.table)} entries')
        for k, v in self.table.items():
            (flags, func) = v
            func(k)

    def _populate(self):
        for i in range(len(self.DISPATCH_TABLE)):
            self._lookup(i, self.DISPATCH_TABLE[i])

    def _lookup(self, n, f):
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
