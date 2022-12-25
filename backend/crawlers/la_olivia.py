from datetime import date
from typing import List, Type

from url_mapping import UrlMapping
from crawlers import BaseCrawler
from bs4 import BeautifulSoup
from crawler import Crawler
from dto.menu_dto import MenuDto


class LaOliviaCrawler(BaseCrawler):
    def get_menu(self, soup: BeautifulSoup, restaurant_id: str, k: str, f) -> MenuDto:
        menu = soup.find(name='div', attrs={'id': k}).find('div').find('div')
        name = menu.find('h6').contents[1]
        description = menu.find('p', attrs={'style': 'text-align: center;'}).contents
        description = self.clean(f(description))
        price = self.clean(menu.find_all('h6')[1].contents[0])
        return MenuDto(name=name, date=date.today(), description=description, price=price,
                       restaurant_id=restaurant_id)  # FIXME: add correct date

    def crawl(self, url: UrlMapping) -> list[MenuDto]:
        soup = BeautifulSoup(Crawler.crawl(url.url), 'html.parser')
        return [self.get_menu(soup, url.id, 'sppb-addon-1521457089207', lambda x: f'{x[1]} {x[3]}'),
                self.get_menu(soup, url.id, 'sppb-addon-wrapper-1521457089210', lambda x: f'{x[0]} {x[2]}')]
