from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import re, openpyxl

# Creating Exel file
exel = openpyxl.Workbook()
sheet = exel.active
sheet.title = "Amazon Review"
sheet.append(['Entry Number', 'Ranking', 'Date', 'Comment', 'Helpfulness Count'])

web = webdriver.Chrome()
web.maximize_window()
sleep(1)

web.get('https://www.amazon.com/Apple-MacBook-14-inch-8%E2%80%91core-14%E2%80%91core/product-reviews/B09JQSLL92/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews')

sleep(2)
page_count = 0
comment_count = 0

for i in range(11):
    try:
        page_count += 1
        print(f'[ Page: {page_count} ]')

        sleep(3)
        pageSource = web.page_source
        soup = BeautifulSoup(pageSource, 'html.parser')
        reviews = soup.find('div', id="cm_cr-review_list").find_all('div', class_='a-section celwidget')

        for review in reviews:
            comment_count += 1

            # collect all ratings
            rating = review.find('span', class_='a-icon-alt').text
            f_rating = rating[:3]
            print(f"Rating: {f_rating}")

            # collect all dates
            date = review.find('span', class_='a-size-base a-color-secondary review-date').text
            f_date = date[33:]
            print(f"Date: {f_date}")

            # collect all review contents
            message = review.find('div', class_='a-row a-spacing-small review-data').text
            f_message = message.strip()
            print(f"Message: {f_message}")

            # collect all helpfull counts
            if review.find('span', class_='a-size-base a-color-tertiary cr-vote-text'):
                helpfull_count = review.find('span', class_='a-size-base a-color-tertiary cr-vote-text').text
                if helpfull_count[:3] == 'One':
                    f_helpfull_count = 1
                else:
                    f_helpfull_count = re.sub('[^0-9]', '', helpfull_count)
            else:
                f_helpfull_count = 0
            print(f"Helpfull count: {f_helpfull_count}")

            # add information to the exel sheet
            sheet.append([comment_count, f_rating, f_date, f_message, f_helpfull_count])

            print("\n")
        print("\n\n--------------------------------\n\n")

        # click next button
        web.find_element(by=By.CLASS_NAME, value="a-last").click()

    except:
        continue

# save the exel file
exel.save('Amazon Review.xlsx')
web.close()
