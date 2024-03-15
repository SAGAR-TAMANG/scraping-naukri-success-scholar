import requests
import time
import datetime
import os

import pandas as pd
import numpy as np

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

CHROMEDRIVER_PATH = r'C:\Program Files\chromedriver_win32\chromedriver.exe'
WINDOW_SIZE = "1920,1080"
chrome_options = Options()

CHROMEDRIVER_PATH = r'C:\Program Files\chromedriver_win32\chromedriver.exe'
WINDOW_SIZE = "1920,1080"
chrome_options = Options()

# chrome_options.add_argument("--headless")
chrome_options.binary_location = r"C:\Users\TAMANG\Downloads\Win_1216615_chrome-win\chrome-win\chrome.exe"
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')

service = Service(CHROMEDRIVER_PATH)

def main():
  dff = pd.DataFrame(columns=['Job Title','Description', 'Experience Reqd', 'Company', 'City', 'Salary Range', 'Date Posted', 'URL'])
  driver = webdriver.Chrome(service = service, options = chrome_options)

  url = "https://www.naukri.com/jobs-in-india"
  # Observation: Page1: https://www.naukri.com/it-jobs?k=it Page2: https://www.naukri.com/it-jobs-2
  driver.get(url)


  time.sleep(3)
  try: 
    driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div[1]/div/section[2]/div[1]/div[2]/span/span[2]/p').click()
    driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div[1]/div/section[2]/div[1]/div[2]/span/span[2]/ul/li[2]').click()
  except Exception as e:
    pass

  # time.sleep(3)
  pages = np.arange(1,250)

  for pages in pages:
    soup = BeautifulSoup(driver.page_source,'html5lib')
    results = soup.find(id='listContainer')
    job_elems = results.find_all('div', class_='srp-jobtuple-wrapper')
    for job_elem in job_elems:
      # Post Title
      T = job_elem.find('a',class_='title')
      Title=T.text

      # Description
      try:
        D = job_elem.find('span', class_='job-desc')
        Description = D.text
      except Exception as e:
        Description = None
      
      # Experience  
      E = job_elem.find('span', class_='expwdth')
      if E is None:
        Exp = "Not-Mentioned"
      else:
        Exp = E.text
      
      # Company
      C = job_elem.find('a', class_='comp-name')
      Company=C.text
      
      # City
      try:
        C = job_elem.find('span', class_='locWdth')
        City=C.text
      except Exception as e:
        City = None

      # Salary Range
      S = job_elem.find('span', 'ni-job-tuple-icon ni-job-tuple-icon-srp-rupee sal')
      Salary=S.text
      print("Salary: ", Salary)

      # Date Posted
      D = job_elem.find('span', class_='job-post-day')
      try: 
        if D == 'Just Now':
          Date = 'Today'
        else:
          Date=D.text
      except Exception as e:
        Date = None      
      
      U = job_elem.find('a',class_='title').get('href')
      URL = U

      dff = pd.concat([dff, pd.DataFrame([[Title, Description, Exp, Company, City, Salary, Date, URL]], columns = ['Job Title','Description', 'Experience Reqd', 'Company', 'City', 'Salary Range', 'Date Posted', 'URL'])], ignore_index=True)
      print(dff)

      dff.to_excel(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', "NaukriJobListing_" + str(datetime.date.today()) + ".xlsx"), index=False)

    driver.execute_script("window.scrollTo(0,(document.body.scrollHeight) - 1500)")

    time.sleep(0.75)

    driver.find_element(By.XPATH, '//*[@id="lastCompMark"]/a[2]/span').click()

    time.sleep(3)

  print("*********************CONCLUSION: FINISHED FETCHING DATA FROM NAUKRI.COM*********************")

  # Closing the Driver
  driver.close()

main()