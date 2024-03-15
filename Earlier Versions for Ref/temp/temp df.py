import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# pages = int(input('NUMBER OF PAGES WORTH OF DATA: '))

dff = pd.DataFrame(columns=['Job Title','Posted', 'Company','URL'])

url = "https://www.naukri.com/jobs-in-india"
# Observation: Page1: https://www.naukri.com/it-jobs Page2: https://www.naukri.com/it-jobs-2

# page = requests.get(url)
# print(page.text)

# Making the Driver Headless: (next 3 lines)
driver = webdriver.Chrome()
# options = Options()
# options.add_argument("--headless=new")
# driver = webdriver.Chrome(options=options)

# time.sleep(3)

# driver = webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source,'html5lib')

# print(soup.prettify())

results = soup.find(class_='list')
job_elems=results.find_all('article', class_='jobTuple')

# print(results)
# print(results.text)
print(job_elems)
driver.close()