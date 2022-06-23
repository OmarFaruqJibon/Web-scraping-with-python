from collections import Counter
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud

amazon_url = "https://www.amazon.com"
url = 'https://www.amazon.com/Apple-MacBook-14-inch-8%E2%80%91core-14%E2%80%91core/product-reviews/B09JQSLL92/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
           "Accept-Encoding": "gzip, deflate",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
           "Connection": "close", "Upgrade-Insecure-Requests": "1", }

req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.content, 'html.parser')

last = soup.find('li', class_="a-last")
msg = []

count = 1

while last:
    for i in soup.find_all('div', class_="a-section review aok-relative"):
        comment = i.find('span', class_="a-size-base review-text review-text-content")
        comment_text = comment.text if comment else ""
        msg.append(comment_text.strip())
        count += 1
    try:
        req = requests.get(amazon_url + last.a['href'], headers=headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        last = soup.find('li', class_="a-last")

    except:
        break

data = " ".join(msg)

wordcloud = WordCloud().generate(data)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

wordcloud = WordCloud(max_font_size=40).generate(data)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

data = data.split(" ")
counter = Counter(data)

high = max(counter, key=counter.get)

print(f"High frequency: {high} \n Frequency: {counter[high]}")


