import requests
from bs4 import BeautifulSoup
url = "http://www.baidu.com"
page = requests.get(url, timeout=30)
t_soup = BeautifulSoup(page.content, 'html.parser')
print(page.text)
