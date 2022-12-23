from crawlers import BaseCrawler
from bs4 import BeautifulSoup
from crawler import Crawler
from dto.menu_dto import MenuDto
from dto.restaurant_dto import RestaurantDto
from datetime import datetime, date


class BioCateringSafranCrawler(BaseCrawler):

    def get_menu(self, soup: BeautifulSoup, restaurant_id: str, day: int, f) -> MenuDto:
        menus = soup.find_all('p', attrs={'class': 'elementor-icon-box-description'})
        i = 0
        for menu in menus:
            if i == day:
                day_menu = self.clean(menu.contents[0].replace("\t", "").replace("\n", ""))
                break
            i += 1
        return MenuDto(name=day_menu, date=date.today(), description=day_menu,
                       price="8 Euro - 15 Euro", restaurant_id=restaurant_id)  # FIXME add correct date!

    def crawl(self, restaurant: RestaurantDto) -> list[MenuDto]:
        soup = BeautifulSoup(Crawler.crawl(restaurant.lunch_source), 'html.parser')
        result = list[MenuDto]
        day = datetime.weekday(datetime.now())
        if day < 7:  # Ohne Sonntag
            menu = self.get_menu(soup, restaurant.id, day, lambda x: f'{x[1]} {x[3]}')
            if menu.name != 'Ruhetag':
                result.append(menu)
        return result
