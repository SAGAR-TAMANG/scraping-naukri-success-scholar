import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np

pages = np.arange(1,11)
dff = pd.DataFrame(columns=['Job Title','Posted', 'Company','URL'])


for pages in pages:
  url = "https://www.naukri.com/it-jobs" + "-" + str(pages)
  # Observation: Page1: https://www.naukri.com/it-jobs?k=it Page2: https://www.naukri.com/it-jobs-2

  page = requests.get(url)
  # print(page.text)

  driver = webdriver.Chrome()
  driver.get(url)

  time.sleep(3)

  soup = BeautifulSoup(driver.page_source,'html5lib')

  # print(soup.prettify())

  driver.close()

  results = soup.find(class_='list')
  job_elems=results.find_all('article', class_='jobTuple')

  print(job_elems)