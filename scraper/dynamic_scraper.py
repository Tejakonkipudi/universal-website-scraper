from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from .base_scraper import BaseScraper

class DynamicScraper(BaseScraper):
    def fetch(self):
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get(self.url)
        html = driver.page_source
        driver.quit()
        return html

    def parse(self):
        html = self.fetch()
        soup = BeautifulSoup(html, "lxml")
        data = {}

        for field, selector in self.rules.items():
            element = soup.select_one(selector)
            data[field] = element.text.strip() if element else None

        return data
