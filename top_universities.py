import requests, openpyxl
from bs4 import BeautifulSoup

excle = openpyxl.Workbook()
sheet = excle.active
sheet.title = "Top Rated Books"
sheet.append(["Index", "Name", "Price"])

source_url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'
res = requests.get(source_url)
soup = BeautifulSoup(res.text, 'html.parser')

books = soup.find('ol', class_="row").find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
count = 0
for book in books:
    count += 1
    name = book.find('article', class_="product_pod").h3.a.text

    price = book.find('div', class_="product_price").find('p', class_="price_color").text
    # print(count, name, price)
    sheet.append([count, name, price])

excle.save("Top Rated Books.xlsx")
