import json
from os import getcwd, name as osname
from os.path import exists


class UrlRegistry(object):
    """
    This class represents a registry of URLs.
    """
    SEPARATOR = '\\' if osname == 'nt' else '/'
    URL_FILE = f'{getcwd()}{SEPARATOR}url_registry.json'

    def __init__(self, *opt_urls):
        """
        Initialize the URL registry. Loads the URLs from a JSON file (url_registry.json) in the current working directory,
        or an empty list if the file does not exist. Any additional URLs provided as arguments will also be added to
        the registry.

        Parameters:
        *opt_urls (str): Optional URL(s) to add to the registry.
        """
        try:
            print(f'Loading urls from: {self.URL_FILE}')
            with open(self.URL_FILE) as f:
                self._urls = json.loads(f.read()) if exists(self.URL_FILE) else []
        except Exception as e:
            print(f'Failed to load urls from JSON: {self.URL_FILE}')
            self._urls = []
            raise e
        finally:
            for url in opt_urls:
                self._urls.append(url)
            self._urls = [(lambda x: x.lower())(x) for x in self._urls]
            for i in range(len(self._urls)):
                print(f'Url #{i}: \'{self._urls[i]}\'')
            print(f'URL registry online {len(self._urls)} available')

    def lookup(self) -> int:
        """
        Look up the number of URLs in the registry.

        Returns:
        int: The number of URLs in the registry.
        """
        i: int = 0
        for url in self._urls:
            print(url)
            i += 1
        return i

    @property
    def get_urls(self):
        """
        Get the URLs in the registry.

        Returns:
        List[str]: A list of the URLs in the registry.
        """
        return self._urls
