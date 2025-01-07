from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from pprint import pprint

# Scrape addresses, prices and links
response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
data = response.text

soup = BeautifulSoup(data, features="html.parser")


addresses = [address.get_text().strip().replace('|', '') for address in soup.find_all("address")]
prices = [price.get_text().replace('+', '') for price in soup.find_all('span', {'data-test': 'property-card-price'})]
links = [link.get('href') for link in soup.find_all('a', {'data-test': 'property-card-link', 'tabindex': 0 })]


# Fill in form using Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(options=chrome_options)


for i in range(len(addresses)):
    driver.get("https://forms.gle/orfMeYYWFABMdVsj9")
    driver.maximize_window()

    time.sleep(1)
    all_entries = driver.find_elements(By.XPATH, value='//input[@type="text"]')

    all_entries[0].click()
    all_entries[0].send_keys(addresses[i])

    all_entries[1].click()
    all_entries[1].send_keys(prices[i])

    all_entries[2].click()
    all_entries[2].send_keys(links[i])

    submit_btn = driver.find_element(By.XPATH, value='//span[text()="Изпращане"]')
    submit_btn.click()
    time.sleep(1)


driver.quit()