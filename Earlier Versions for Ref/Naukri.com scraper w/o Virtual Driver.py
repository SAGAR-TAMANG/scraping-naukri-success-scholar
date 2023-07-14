import requests
from bs4 import BeautifulSoup


url = 'https://www.naukri.com/it-jobs'
page = requests.get(url)

print(page.text)
soup = BeautifulSoup(page.text, 'html5lib')

cards = soup.find_all('dev', 'list')
print(cards)