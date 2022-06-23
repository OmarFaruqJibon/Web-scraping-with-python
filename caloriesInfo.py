from gevent import monkey
monkey.patch_all()
import gevent, requests, bs4, csv
from gevent.queue import Queue

work = Queue()
names = []
url_list = []

headers={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'
}

res = requests.get('https://www.calories.info/', headers=headers)
bs_res = bs4.BeautifulSoup(res.text, 'html.parser')
categories = bs_res.find('div', class_='menu-calorie-tables-container').find_all('a')

for each_cate in categories:
    name = each_cate.text
    names.append(name)
    url = each_cate['href']
    url_list.append(url)

#print(names,url_list)

for url in url_list:
    work.put_nowait(url)


def crawler():
    while not work.empty():
        url = work.get_nowait()
        # print(url)
        res = requests.get(url, headers=headers)
        bs_res_foods=bs4.BeautifulSoup(res.text, 'html.parser')
        # print(bs_res_foods)
        foods = bs_res_foods.find_all('tr', class_='kt-row')

        for single_food in foods:
            food_name = single_food.find('a').text
            print(food_name)

            food_url = single_food.find('a')['href']
            print(food_url)

            food_serving = single_food.find('td', class_='serving portion').find('data').text+'g'
            print(food_serving)

            food_calories = single_food.find('td', class_='kj').find('data').text+'KJ'
            print(food_calories)

            print("\n------------------\n")

            writer.writerow([food_name, food_url, food_serving, food_calories])


csv_file = open('Food&Calories.csv', 'w', newline='')
writer = csv.writer(csv_file)
writer.writerow(['name', 'url', 'serving', 'calories'])

tasks_list = []
for x in range(len(url_list)):
    task = gevent.spawn(crawler)
    tasks_list.append(task)
gevent.joinall(tasks_list)

print(len(tasks_list))


