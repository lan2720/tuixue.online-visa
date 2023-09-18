import cloudscraper
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')
options.add_argument('disable-gpu')
options.add_argument('no-sandbox')
options.add_argument('disable-dev-shm-usage')

driver = webdriver.Chrome(options=options,
                          service=ChromeService(ChromeDriverManager().install()))
# Create cloudscraper instance
scraper = cloudscraper.create_scraper(browser=driver)
# Or: scraper = cloudscraper.CloudScraper() # CloudScraper inherits from requests.Session
with open("cloud.html", "w") as f:
    f.write(scraper.get("https://portal.ustraveldocs.com").text)