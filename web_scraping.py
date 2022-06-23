import requests
from bs4 import BeautifulSoup

# url = 'https://quickemailverification.com/blog/wp-content/uploads/2020/05/Top-10-Web-Scraping-Tools-and-Software-Compared.jpg'


url = "https://www.swpu.edu.cn/en/index/Admissions1/Undergraduate.htm"

res = requests.get(url)
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'html.parser')

items = soup.find_all('p', class_='1')
# print(items)


for item in items:
    print(item.find('span', style='line-height: 150%; font-family: \'times new roman\',serif; color: black; font-size: 14px; mso-themecolor: text1').text)




