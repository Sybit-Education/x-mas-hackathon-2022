import logging
import os
import urllib

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class Crawler:
    def crawl(url: str) -> str:
        logging.info(f'Crawling: \'{url}\'')

        if 'HTTP_PROXY' in os.environ and 'HTTPS_PROXY' in os.environ:
            logging.info("Using environment var HTTP[S]_PROXY for requests")
            proxy = urllib.request.ProxyHandler({'http': os.environ['HTTP_PROXY'], 'https': os.environ['HTTPS_PROXY']})
            opener = urllib.request.build_opener(proxy)
            urllib.request.install_opener(opener)
        else:
            logging.info("No environment vars HTTP[S]_PROXY defined for crawler")

        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        response = session.get(url)
        txt = response.content.decode("utf-8")

        return txt
