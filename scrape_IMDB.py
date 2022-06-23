import requests, openpyxl
from bs4 import BeautifulSoup

exel = openpyxl.Workbook()
sheet = exel.active
sheet.title = "Top Rated Movies"
sheet.append(['Rank', 'Name', 'Year', 'Rating'])




source_url = 'https://www.imdb.com/chart/top/'
res = requests.get(source_url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

movies = soup.find('tbody', class_="lister-list").find_all('tr')


for movie in movies:
    rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]

    name = movie.find('td', class_="titleColumn")
    x = name.find('a').text

    year = movie.find('td', class_="titleColumn").span.text.strip('()')

    rating = movie.find('td', class_="imdbRating").strong.text

    # print(rating)
    sheet.append([rank, x, year, rating])

exel.save('IMDB top rated movies.xlsx')
