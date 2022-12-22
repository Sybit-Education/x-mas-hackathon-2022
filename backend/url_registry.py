from services.restaurant import get_all_restaurants
from os import getcwd, name as osname

class UrlEntry:
    def __init__(self, id, url):
        self.id = id
        self.url = url

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
        restaurants = get_all_restaurants()
        self._urls = []
        for r in restaurants:
            self._urls.append(UrlEntry(id=r.crawler_id, url=r.lunch_source))
        for url in opt_urls:
            self._urls.append(url)
        for i in range(len(self._urls)):
            print(f'Url #{i}: \'{self._urls[i].url}\'')
        print(f'URL registry online {len(self._urls)} available')

    @property
    def get_urls(self):
        """
        Get the URLs in the registry.

        Returns:
        List[str]: A list of the URLs in the registry.
        """
        return self._urls
