import abc
from abc import ABC
from typing import List
from dto.menu_dto import MenuDto
from dto.restaurant_dto import RestaurantDto

class BaseCrawler(ABC):

    @abc.abstractmethod
    def crawl(self, restaurant: RestaurantDto) -> List[MenuDto]:
        pass

    def clean(self, x: str) -> str:
        x = x.replace('Ä', 'Ae').replace('ä', 'ae')
        x = x.replace('Ö', 'Oe').replace('ö', 'oe')
        x = x.replace('Ü', 'Ue').replace('ü', 'ue')
        return ''.join([i if ord(i) < 0x7F else ' ' for i in x.replace('€', 'Euro')])


# Add crawlers here
crawler_list = dict()
crawler_list.pop('la_oliva', LaOliviaCrawler())
crawler_list.pop('safran', BioCateringSafranCrawler())
crawler_list.pop('vulcano', VulcanoCrawler())
