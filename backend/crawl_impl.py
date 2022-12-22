from bs4 import BeautifulSoup
from dto import *
from crawler import Crawler
from dto.menu_dto import MenuDto
from dto.restaurant_dto import RestaurantDto


def clean(x: str) -> str:
    return ''.join([i if ord(i) < 0x7F else ' ' for i in x.replace('€', 'Euro')])


def get_menu(soup: BeautifulSoup, k: str, f) -> MenuDto:
    menu = soup.find(name='div', attrs={'id': k}).find('div').find('div')
    name = menu.find('h6').contents[1]
    description = menu.find('p', attrs={'style': 'text-align: center;'}).contents
    description = clean(f(description))
    price = clean(menu.find_all('h6')[1].contents[0])
    return MenuDto(name=name, description=description, price=price)


def crawl_la_olivia(url: str) -> RestaurantDto:
    soup = BeautifulSoup(Crawler.crawl(url), 'html.parser')
    result = RestaurantDto()
    result.name = 'La Olivia'
    result.menus.append(get_menu(soup, 'sppb-addon-1521457089207', lambda x: f'{x[1]} {x[3]}'))
    result.menus.append(get_menu(soup, 'sppb-addon-wrapper-1521457089210', lambda x: f'{x[0]} {x[2]}'))
    return result
