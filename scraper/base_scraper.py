from abc import ABC, abstractmethod

class BaseScraper(ABC):
    def __init__(self, url, rules):
        self.url = url
        self.rules = rules

    @abstractmethod
    def fetch(self):
        pass

    @abstractmethod
    def parse(self):
        pass
