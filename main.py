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
workbook = openpyxl.Workbook()
book = workbook.active
book.title = "Amazon Review"
book.append(['Index', 'Rating', 'Date', 'Comment', 'Helpfull Count'])
x = 0

for i in range(11):
    try:
        sleep(3)
        pageSource = web.page_source
        soup = BeautifulSoup(pageSource, 'html.parser')
        comments = soup.find('div', id="cm_cr-review_list").find_all('div', class_='a-section celwidget')
        for comment in comments:
            x = x + 1
            comment_rating = comment.find('span', class_='a-icon-alt').get_text()
            print(comment_rating)
            date = comment.find('span', class_='a-size-base a-color-secondary review-date').get_text()
            print(date)
            comment_content = comment.find('div', class_='a-row a-spacing-small review-data').text.strip()
            print(comment_content)
            if comment.find('span', class_='a-size-base a-color-tertiary cr-vote-text'):
                help = comment.find('span', class_='a-size-base a-color-tertiary cr-vote-text').text
            print(help)
            print("\n\n")
            book.append([x, comment_rating, date, comment_content, help])
        web.find_element(by=By.CLASS_NAME, value="a-last").click()
    except:
        break
workbook.save('amazon.xlsx')
print('Total amount of comments: ', i* 10)
web.close()
