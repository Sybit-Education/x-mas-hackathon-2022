class DispatchFlags:
    NONE = 0 << 0
    SKIP = 1 << 0

class UrlMapping:
    def __init__(self, id: str, delegate, url: str, flags: int = DispatchFlags.NONE):
        self.id = id
        self.delegate = delegate
        self.url = url
        self.flags = flags
