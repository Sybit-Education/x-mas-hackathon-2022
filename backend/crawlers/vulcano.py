import re
from datetime import date
from typing import List, Type

from crawlers import BaseCrawler
from bs4 import BeautifulSoup, PageElement
from crawler import Crawler
from dto.menu_dto import MenuDto
from dto.restaurant_dto import RestaurantDto
from price_parser import Price


class VulcanoCrawler(BaseCrawler):
    def get_menu(self, menu: PageElement, restaurant_id: str, f) -> MenuDto:
        name = menu.text.strip()
        price = Price.fromstring(menu.text[-8:], currency_hint="€", decimal_separator=",")
        if price and price.amount:
            price_str = price.amount_text + " " + price.currency if price.currency is not None else ''
            name = menu.text[:-(len(price_str)+1)].strip()
        else:
            price_str = ''
        return MenuDto(name=name, date=date.today(), description='', price=price_str, restaurant_id=restaurant_id)  # FIXME: add correct date & price

    def crawl(self, restaurant: RestaurantDto) -> Type[list[MenuDto]]:
        result = list()

        soup = BeautifulSoup(Crawler.crawl(restaurant.lunch_source), "html.parser")
        section = soup.find(name='section', attrs={'class': 'content14'})
        menu_list = section.find('ul')
        for menu in menu_list.children:
            if menu.text.strip() and menu.text.startswith('M'):
                result.append(self.get_menu(menu, restaurant.id, lambda x: f'{x[1]} {x[3]}'))

        return result
