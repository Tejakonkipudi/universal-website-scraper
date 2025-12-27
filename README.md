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
## Clone the Repository
git clone https://github.com/Tejakonkipudi/universal-website-scraper.git
cd universal-website-scraper
## Create Output Folder (Important)
mkdir output
## Step 3: Install Required Python Packages
🔹 Windows
pip install -r requirements.txt
If pip does not work:
python -m pip install -r requirements.txt
## 🔹 Linux (Ubuntu / Debian)
pip3 install -r requirements.txt
If pip is missing:
sudo apt install python3-pip
pip3 install -r requirements.txt
## 3️⃣ Add ChromeDriver to PATH
macOS / Linux:
sudo mv chromedriver /usr/local/bin
sudo chmod +x /usr/local/bin/chromedriver
## ⚙️ Step 5: Configure Website to Scrape
configs/sample_config.json
{ example Configuration :
{
"url": "https://example.com",
"type": "static",
"rules": {
"title": "h1",
"description": "p"
}
}
## Configuration Fields
url → Website URL
type → static or dynamic
rules → CSS selectors for data extraction
## ▶️ Step 6: Run the Scraper**
Windows**
python main.py
macOS / Linux
python3 main.py
## 📤 Step 7: View Output
output/scraped_data.json
output/scraped_data.csv 
saved in those above files.
you can see the results of website details.
