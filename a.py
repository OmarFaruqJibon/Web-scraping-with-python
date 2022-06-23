from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
from bs4 import BeautifulSoup
from time import sleep

source = webdriver.Chrome()
source.maximize_window()
sleep(1)

source.get('https://www.amazon.com/Apple-MacBook-14-inch-8%E2%80%91core-14%E2%80%91core/product-reviews/B09JQSLL92/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews')
sleep(2)

file = openpyxl.Workbook()
page = file.active
page.title = "Review"
page.append(['Entry Number', 'Ranking', 'Date', 'Comment', 'Helpfulness Count'])

count = 0
for i in range(11):
    try:
        sleep(3)
        pageSource = source.page_source
        soup = BeautifulSoup(pageSource, 'html.parser')
        items = soup.find('div', id="cm_cr-review_list").find_all('div', class_='a-section celwidget')

        for item in items:
            count+=1
            rate = item.find('span', class_='a-icon-alt').text[:3]

            date = item.find('span', class_='a-size-base a-color-secondary review-date').text[33:]

            content = item.find('div', class_='a-row a-spacing-small review-data').text.strip()

            if item.find('span', class_='a-size-base a-color-tertiary cr-vote-text'):
                helpfull = item.find('span', class_='a-size-base a-color-tertiary cr-vote-text').text

            print(rate)
            print(date)
            print(content)
            print(helpfull)

            page.append([count, rate, date, content, helpfull])
            print("\n\n")

        source.find_element(by=By.CLASS_NAME, value="a-last").click()
    except:
        break
file.save('review.xlsx')
source.close()
