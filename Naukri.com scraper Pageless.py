import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By

# pages = int(input('NUMBER OF PAGES WORTH OF DATA: '))

dff = pd.DataFrame(columns=['Job Title','Posted', 'Company','URL'])

url = "https://www.naukri.com/jobs-in-india"
# Observation: Page1: https://www.naukri.com/it-jobs Page2: https://www.naukri.com/it-jobs-2

# page = requests.get(url)
# print(page.text)

# Making the Driver Headless: (next 3 lines)
driver = webdriver.Chrome()
driver.headless = True

# time.sleep(3)

# driver = webdriver.Chrome()
driver.get(url)
driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div[1]/div/section[2]/div[1]/div[2]/span/span[2]/p').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div[1]/div/section[2]/div[1]/div[2]/span/span[2]/ul/li[2]').click()

time.sleep(3)

soup = BeautifulSoup(driver.page_source,'html5lib')

# print(soup.prettify())

results = soup.find(class_='list')
job_elems=results.find_all('article', class_='jobTuple')

pages = np.arange(0,25)

# print(job_elems)
# for x in range(0,pages):
for pages in pages:
  for job_elem in job_elems:
    # URL to apply for the job     
    URL = job_elem.find('a',class_='title ellipsis').get('href')
    # print(URL)
    
    # Post Title
    T = job_elem.find('a',class_='title ellipsis')
    Title=T.text
    # print("Job Title: " + Title.text)
    
    C = job_elem.find('a', class_='subTitle ellipsis fleft')
    Company=C.text
    # print("Company: " + Company.text)

    E = job_elem.find('span', class_='ellipsis fleft expwdth')
    Exp=E.text
    # print('Experience: ' + Exp.text)
    # print(" "*2)

    H= job_elem.find('span', class_='fleft postedDate')
    History=H.text

    # df=df.append({'Title':Title, 'Company':Company,'URL':URL}, ignore_index = True)
    # df = pd.DataFrame([[Title, Company, URL]], columns=['Title','Company','URL'])
    dff = pd.concat([dff, pd.DataFrame([[Title, History, Company, URL]], columns = ['Job Title','Posted', 'Company','URL'])], ignore_index=True)
    # Second Way using Concat:
    # df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    # df3 = pd.concat([df3, df2], ignore_index=True)

    # dff.to_csv("Naukri.com_Data_Collection.csv", index = False)
    dff.to_excel("All_Output.xlsx", index = False)
    
    print(dff)

    driver.execute_script("window.scrollTo(0, Y)")

    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/div/section[2]/div[3]/div/a[2]/span').click()
    time.sleep(3)





# driver.close() #END OPERATION