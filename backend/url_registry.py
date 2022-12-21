class UrlRegister(object):
    def __init__(self):
        self.urls = []

    def lookup(self) -> int:
        i: int = 0
        for url in self.urls:
            print(url)
            i += 1
        return i
