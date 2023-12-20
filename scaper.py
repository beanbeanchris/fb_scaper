import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import datetime
from bs4 import BeautifulSoup
import pandas as pd 
from dotenv import load_dotenv
import os
EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("MY_PASSWORD")
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# Create an empty DataFrame with these columns
columns = ['date_posted', 'location', 'land_area', 'price']
df = pd.DataFrame(columns=columns)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)  
driver.get("https://www.facebook.com")
driver.maximize_window()
sleep(2)

cookies = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="_42ft _4jy0 _9o-t _4jy3 _4jy1 selected _51sy"]'))).click()
email = driver.find_element_by_id("email")
email.send_keys(EMAIL)





