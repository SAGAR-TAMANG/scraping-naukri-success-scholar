import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException



pages = np.arange(1,11)
dff = pd.DataFrame(columns=['Job Title','Posted', 'Company','URL'])



url = "https://www.naukri.com/it-jobs" + "-" + str(pages)
# Observation: Page1: https://www.naukri.com/it-jobs?k=it Page2: https://www.naukri.com/it-jobs-2


page = requests.get(url)
# print(page.text)

# Making the Driver Headless: (next 3 lines)
driver = webdriver.Chrome()
driver.headless = True

# driver = webdriver.Chrome()
driver.get(url)


driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/div/section[3]/div[1]/div[2]/span/span[2]').click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='root']/div[4]/div/div/section[3]/div[1]/div[2]/span/span[2]/ul/li[2]").click()

time.sleep(10)
# print(soup.prettify())
