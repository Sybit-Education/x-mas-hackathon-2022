import abc
from abc import ABC
from dto.restaurant_dto import RestaurantDto

class BaseCrawler(ABC):
    @abc.abstractmethod
    def crawl(self, url: str) -> RestaurantDto:
        pass

    def clean(self, url: str) -> str:
        return ''.join([i if ord(i) < 0x7F else ' ' for i in url.replace('€', 'Euro')])