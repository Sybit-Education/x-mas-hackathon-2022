import json
import os


class UrlRegister(object):
    URL_FILE = 'url_registry.json'

    def __init__(self, *opt_urls):
        try:
            self.urls = json.loads(self.URL_FILE) if os.path.exists(self.URL_FILE) else []
        except Exception as e:
            print(f'Failed to load urls from JSON: {self.URL_FILE}')
            self.urls = []
            raise e
        finally:
            for url in opt_urls:
                self.urls.append(url)
            print(f'URL registry online {self.urls} available')

    def lookup(self) -> int:
        i: int = 0
        for url in self.urls:
            print(url)
            i += 1
        return i
