from crawlers import la_olivia, biocatering_safran, vulcano


def register_crawlers():
    return {
        'la_oliva': lambda restaurant: la_olivia.LaOliviaCrawler().crawl(restaurant),
        'biocatering_safran': lambda restaurant: biocatering_safran.BioCateringSafranCrawler().crawl(restaurant),
        'vulcano': lambda restaurant: vulcano.VulcanoCrawler().crawl(restaurant)
    }
