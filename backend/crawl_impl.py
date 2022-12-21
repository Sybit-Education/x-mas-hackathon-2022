from bs4 import BeautifulSoup
from dto import *
from crawler import Crawler


def crawl_la_olivia(url: str) -> RestaurantDto:
    soup = BeautifulSoup(Crawler.crawl(url), 'html.parser')
    result = RestaurantDto()
    result.name = soup.find('href')
    return result
