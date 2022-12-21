import json
from os import getcwd, name as osname
from os.path import exists


class UrlRegistry(object):
    SEPARATOR = '\\' if osname == 'nt' else '/'
    URL_FILE = f'{getcwd()}{SEPARATOR}url_registry.json'

    def __init__(self, *opt_urls):
        try:
            print(f'Loading urls from: {self.URL_FILE}')
            with open(self.URL_FILE) as f:
                self.urls = json.loads(f.read()) if exists(self.URL_FILE) else []
        except Exception as e:
            print(f'Failed to load urls from JSON: {self.URL_FILE}')
            self.urls = []
            raise e
        finally:
            for url in opt_urls:
                self.urls.append(url)
            self.urls = [(lambda x: x.lower())(x) for x in self.urls]
            for i in range(len(self.urls)):
                print(f'Url #{i}: \'{self.urls[i]}\'')
            print(f'URL registry online {len(self.urls)} available')

    def lookup(self) -> int:
        i: int = 0
        for url in self.urls:
            print(url)
            i += 1
        return i
