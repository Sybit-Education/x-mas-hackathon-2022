import requests


class Crawler:
    def crawl(url: str) -> str:
        print(f'Crawling: \'{url}\'')
        page = requests.get(url)
        return page.text
