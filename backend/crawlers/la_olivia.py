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
        price = self.clean(menu.find_all('h6')[1].contents[0])
        return MenuDto(name=name, date="", description=description, price=price, restaurant_id=restaurant_id)  # FIXME: add correct date

    def crawl(self, restaurant: RestaurantDto) -> list[MenuDto]:
        soup = BeautifulSoup(Crawler.crawl(restaurant.lunch_source), 'html.parser')
        result = list[MenuDto]
        result.append(self.get_menu(soup, restaurant.id, 'sppb-addon-1521457089207', lambda x: f'{x[1]} {x[3]}'))
        result.append(self.get_menu(soup, restaurant.id, 'sppb-addon-wrapper-1521457089210', lambda x: f'{x[0]} {x[2]}'))
        return result
