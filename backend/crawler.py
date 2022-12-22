import os
import urllib

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class Crawler:
    def crawl(url: str) -> str:
        print(f'Crawling: \'{url}\'')

        if 'HTTP_PROXY' in os.environ and 'HTTPS_PROXY' in os.environ:
            proxy = urllib.request.ProxyHandler({'http': os.environ['HTTP_PROXY'], 'https': os.environ['HTTPS_PROXY']})
            opener = urllib.request.build_opener(proxy)
            urllib.request.install_opener(opener)

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
