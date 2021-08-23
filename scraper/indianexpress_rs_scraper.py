from abstract_scraper import AbstractScraper
import requests
from bs4 import BeautifulSoup


class IndiaExpressScraper(AbstractScraper):

    url = "https://indianexpress.com/"

    def get_name(self):
        return 'IndianExpress.rs'

    def fetch_links(self):
        soup = BeautifulSoup(requests.get(self.url).content, 'html.parser')
        return soup.find_all('a')

    def apply_filter(self, data, filters):
        keywords = filters.get('keywords')
        all_unique_link = set()
        for link in data:
            if link.get('href') != '#':
                link_text = link.get('href')
                if link_text.startswith("/"):
                    link_text = self.url + link_text
                for keyword in keywords:
                    if keyword in link_text:
                        all_unique_link.add(link_text)
        return all_unique_link

    def process_link(self, link):
        # url, title,news content, event timestamp, keyword matched
        data = {
            'url': link,
            'title': 'title',
            'news content': 'location',
            'event timestamp': 'August 22, 2021 10:08 IST',
            'keyword matched': 'coronavirus',
        }
        return data
