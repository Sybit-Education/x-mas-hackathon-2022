import abc
from abc import ABC
from dto.restaurant_dto import RestaurantDto

class BaseCrawler(ABC):
    @abc.abstractmethod
    def crawl(self, url: str) -> RestaurantDto:
        pass

    def clean(self, x: str) -> str:
        x = x.replace('Ä', 'Ae').replace('ä', 'ae')
        x = x.replace('Ö', 'Oe').replace('ö', 'oe')
        x = x.replace('Ü', 'Ue').replace('ü', 'ue')
        return ''.join([i if ord(i) < 0x7F else ' ' for i in x.replace('€', 'Euro')])