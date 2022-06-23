from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup

web = webdriver.Chrome()
web.maximize_window()
sleep(1)
web.get('https://www.chegg.com/homework-help/questions-and-answers/126-word-frequency-bar-chart-word-cloud-shakespeare-s-hamlet-using-techniques-learned-chap-q85611302?fbclid=IwAR2wy8cBJeu_HnrVKqGrdmOFioek_2aUdNJJI6aFfqnnqMho_B003uuJM6E')
sleep(2)

try:
    sleep(3)
    pageSource = web.page_source
    soup = BeautifulSoup(pageSource, 'html.parser')
    cont = soup.find('section', class_="sc-ezipRf bSkNQK").find('div', class_='sc-mlOqW flXQvI')

    print(cont)




except:
    print("error")

web.close()
