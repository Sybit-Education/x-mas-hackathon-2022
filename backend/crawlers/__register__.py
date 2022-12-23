from crawlers import la_olivia, biocatering_safran


def register_crawlers():
    return {
        'la_oliva': lambda url: la_olivia.LaOliviaCrawler().crawl(url),
        'safran': lambda url: biocatering_safran.BioCateringCrawler().crawl(url)
    }
