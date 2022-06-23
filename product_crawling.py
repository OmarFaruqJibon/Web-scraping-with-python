import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Apple-MacBook-14-inch-8%E2%80%91core-14%E2%80%91core/product-reviews/B09JQSLL92/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

res = requests.get(url)
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text,'html.parser')


items = soup.find_all('div', class_='genome-widget-row')



print(items)

