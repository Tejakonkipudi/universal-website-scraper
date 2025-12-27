import json
from scraper.static_scraper import StaticScraper
from scraper.dynamic_scraper import DynamicScraper
from scraper.utils import save_json, save_csv

def main():
    with open("configs/sample_config.json") as f:
        config = json.load(f)

    url = config["url"]
    rules = config["rules"]
    scraper_type = config["type"]

    if scraper_type == "dynamic":
        scraper = DynamicScraper(url, rules)
    else:
        scraper = StaticScraper(url, rules)

    data = scraper.parse()

    save_json(data, "output/scraped_data.json")
    save_csv(data, "output/scraped_data.csv")

    print("Scraping completed successfully.")

if __name__ == "__main__":
    main()
