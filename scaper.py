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
load_dotenv()
import os
from selenium.webdriver.chrome.service import Service



EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("MY_PASSWORD")
FB_GROUP = os.getenv("FB_GROUP_SITE")
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# # Create an empty DataFrame with these columns
columns = ['date_posted', 'location', 'land_area', 'price']
df = pd.DataFrame(columns=columns)

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.facebook.com")
driver.maximize_window()
sleep(2)

email = driver.find_element(By.ID, "email")
email.send_keys(EMAIL)
sleep(1)
print(EMAIL)
password = driver.find_element(By.NAME, "pass")
password.send_keys(PASSWORD)
sleep(1)
print(PASSWORD)
login = driver.find_element(By.NAME, "login")
login.click()
sleep(1)
driver.get(FB_GROUP) # change group here
sleep(4)





