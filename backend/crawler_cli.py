import argparse
import logging
import logging.config

from crawler import Crawler
from crawlers.biocatering_safran import BioCateringSafranCrawler
from dto.restaurant_dto import RestaurantDto

"""
Update following variables to test specific restaurant crawler:

restaurant_crawler_to_test: Class of crawler.
url_to_crawl: hyperlink to page which should be analyzed
"""
restaurant_crawler_to_test = BioCateringSafranCrawler()
url_to_crawl = "https://biocatering-safran.de/"

def main():
    """
    CLI program to test crawling implementation for specific restaurant.
    :return: print out the resulting menuDTOs on console to verify.
    """
    content = Crawler.crawl(url_to_crawl)
    logging.info(content)

    logging.info("-----------------------------------------------------------------------------------------------------------------")

    restaurant = RestaurantDto(restaurant_id="cliTest")
    restaurant.name = "CLI Test"
    restaurant.lunch_source = url_to_crawl

    result = restaurant_crawler_to_test.crawl(restaurant=restaurant)
    for menu in result:
        logging.info("Result: %s", menu)


if __name__ == '__main__':
    logging.config.fileConfig('logging.conf')

    main()
