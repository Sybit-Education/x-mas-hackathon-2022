from datetime import date
from typing import List, Type

from price_parser import Price

from crawler_mapping import CrawlerMapping
from crawlers import BaseCrawler
from bs4 import BeautifulSoup
from crawler import Crawler
from dto.menu_dto import MenuDto
from dto.restaurant_dto import RestaurantDto


class LaOliviaCrawler(BaseCrawler):
    def get_menu(self, soup: BeautifulSoup, restaurant_id: str, k: str, f) -> MenuDto:
        menu = soup.find(name='div', attrs={'id': k}).find('div').find('div')
        name = menu.find('h6').contents[1]
        description = menu.find('p', attrs={'style': 'text-align: center;'}).contents
        description = self.clean(f(description))
        price = Price.fromstring(self.clean(menu.find_all('h6')[1].contents[0]), decimal_separator=",", currency_hint="Euro")
        if price and price.amount:
            price_str = price.amount_text + " €"
        else:
            price_str=''

        return MenuDto(name=name, date=date.today(), description=description, price=price_str,
                       restaurant_id=restaurant_id)  # FIXME: add correct date

    def crawl(self, restaurant: RestaurantDto) -> list[MenuDto]:
        markup = Crawler.crawl(restaurant.lunch_source)
        soup = BeautifulSoup(markup, 'html.parser')
        return [self.get_menu(soup, restaurant.id, 'sppb-addon-1521457089207', lambda x: f'{x[1]} {x[3]}'),
                self.get_menu(soup, restaurant.id, 'sppb-addon-wrapper-1521457089210', lambda x: f'{x[0]} {x[2]}')]
