from crawlers import la_olivia, biocatering_safran


def register_crawlers():
    return {
        'la_oliva': lambda restaurant: la_olivia.LaOliviaCrawler().crawl(restaurant),
        'safran': lambda restaurant: biocatering_safran.BioCateringCrawler().crawl(restaurant)
    }
