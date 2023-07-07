import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np

#testing the scrollling

dff = pd.DataFrame(columns=['Job Title','Posted', 'Company','URL'])

driver = webdriver.Chrome()

driver.get('https://quotes.toscrape.com/')

time.sleep(1)

driver.execute_script("window.scrollTo(0, Y)")

time.sleep(3)