from crawlers import BaseCrawler
from bs4 import BeautifulSoup
from crawler import Crawler
from dto.menu_dto import MenuDto
from dto.restaurant_dto import RestaurantDto
from datetime import datetime


class BioCateringCrawler(BaseCrawler):

    def get_menu(self, soup: BeautifulSoup, day: int, f) -> MenuDto:
        menus = soup.find_all('p', attrs={'class': 'elementor-icon-box-description'})
        i = 0
        for menu in menus:
            if i == day:
                dayMenu = self.clean(menu.contents[0].replace("\t", "").replace("\n", ""))
                break
            i += 1
        return MenuDto(name=dayMenu, date="", description=dayMenu, price="8 Euro - 15 Euro")  

    def crawl(self, url: str) -> RestaurantDto:
        soup = BeautifulSoup(Crawler.crawl(url), 'html.parser')
        result = RestaurantDto()
        result.name = 'Biocatering Safran'
        day = datetime.weekday(datetime.now())
        if day < 7: # Ohne Sonntag
            menu = self.get_menu(soup, day, lambda x: f'{x[1]} {x[3]}')
            if menu.name != 'Ruhetag':
                result.menus.append(menu)
        return result
