import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class Crawler:
    def crawl(url: str) -> str:
        print(f'Crawling: \'{url}\'')
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        page = session.get(url)
        txt = page.text
        txt = txt.replace('ü', 'ue')
        txt = txt.replace('ä', 'ae')
        txt = txt.replace('ö', 'oe')
        return txt
