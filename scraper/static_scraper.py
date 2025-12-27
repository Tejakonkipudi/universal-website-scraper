import requests
from bs4 import BeautifulSoup
from .base_scraper import BaseScraper

class StaticScraper(BaseScraper):
    def fetch(self):
        response = requests.get(self.url, timeout=10)
        response.raise_for_status()
        return response.text

    def parse(self):
        html = self.fetch()
        soup = BeautifulSoup(html, "lxml")
        data = {}

        for field, selector in self.rules.items():
            element = soup.select_one(selector)
            data[field] = element.text.strip() if element else None

        return data
