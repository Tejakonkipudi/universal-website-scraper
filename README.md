# Universal Website Scraper

A configurable Python-based web scraping system for static and dynamic websites.

## Features
- User-defined scraping rules
- Static & JavaScript-rendered pages
- JSON & CSV output
- Modular and scalable architecture

## Usage
1. Configure `configs/sample_config.json`
2. Run: `python main.py`
## 📌 Prerequisites (All Operating Systems)

Ensure the following are installed:

Python 3.8 or higher

python --version

Git

git --version
📥 Step 1: Clone the Repository
git clone https://github.com/Tejakonkipudi/universal-website-scraper.git
cd universal-website-scraper
📂 Step 2: Create Output Folder (Important)
mkdir output
📦 Step 3: Install Required Python Packages
🔹 Windows
pip install -r requirements.txt

If pip does not work:

python -m pip install -r requirements.txt
🔹 macOS
pip3 install -r requirements.txt

If permission error:

pip3 install --user -r requirements.txt
🔹 Linux (Ubuntu / Debian)
pip3 install -r requirements.txt

If pip is missing:

sudo apt install python3-pip
pip3 install -r requirements.txt
🌐 Step 4: (Optional) Setup Selenium for Dynamic Websites

Only required for dynamic (JavaScript-based) websites.

1️⃣ Install Google Chrome

https://www.google.com/chrome/

2️⃣ Download ChromeDriver

https://chromedriver.chromium.org/downloads

Download the version matching your Chrome browser.

3️⃣ Add ChromeDriver to PATH

Windows: Place chromedriver.exe in the project folder or add it to System PATH

macOS / Linux:

sudo mv chromedriver /usr/local/bin
sudo chmod +x /usr/local/bin/chromedriver
⚙️ Step 5: Configure Website to Scrape

Edit the configuration file:

configs/sample_config.json
Example Configuration
{
  "url": "https://example.com",
  "type": "static",
  "rules": {
    "title": "h1",
    "description": "p"
  }
}
Configuration Fields

url → Website URL

type → static or dynamic

rules → CSS selectors for data extraction

▶️ Step 6: Run the Scraper
Windows
python main.py
macOS / Linux
python3 main.py
📤 Step 7: View Output

Scraped data will be saved in:

output/scraped_data.json

or

output/scraped_data.csv
🧪 Sample Test (Recommended)
{
  "url": "https://en.wikipedia.org/wiki/Web_scraping",
  "type": "static",
  "rules": {
    "title": "h1",
    "description": "div.mw-parser-output > p"
  }
}
❗ Common Errors & Fixes
❌ FileNotFoundError: output/scraped_data.json

✅ Fix:

mkdir output
❌ JSON file showing command not found

✅ Fix:

Do NOT run JSON files in terminal

Only edit them using a text editor

❌ Selenium not working

✅ Fix:

Ensure ChromeDriver version matches Chrome

Ensure ChromeDriver is added to PATH
