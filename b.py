from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import openpyxl

web = webdriver.Chrome()
web.maximize_window()
sleep(1)

web.get('https://www.amazon.com/Apple-MacBook-14-inch-8%E2%80%91core-14%E2%80%91core/product-reviews/B09JQSLL92/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews')
sleep(2)

wb = openpyxl.Workbook()
s = wb.active
s.title = "Amazon"
s.append(['Entry Number', 'Ranking', 'Date', 'Comment', 'Helpfulness Count'])
c = 0

for i in range(11):
    try:
        sleep(3)
        pageSource = web.page_source
        soup = BeautifulSoup(pageSource, 'html.parser')
        ratings = soup.find('div', id="cm_cr-review_list").find_all('div', class_='a-section celwidget')

        for rate in ratings:
            c = c + 1
            comment_rating = rate.find('span', class_='a-icon-alt').text[:3]
            print(comment_rating)
            date = rate.find('span', class_='a-size-base a-color-secondary review-date').text[33:]
            print(date)
            comment_content = rate.find('div', class_='a-row a-spacing-small review-data').text.strip()
            print(comment_content)
            if rate.find('span', class_='a-size-base a-color-tertiary cr-vote-text'):
                h = rate.find('span', class_='a-size-base a-color-tertiary cr-vote-text').text
            print(h)
            s.append([c, comment_rating, date, comment_content, h])
        web.find_element(by=By.CLASS_NAME, value="a-last").click()
    except:
        break
wb.save('amazon.xlsx')
web.close()
