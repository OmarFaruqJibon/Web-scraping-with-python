from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import pynlpir as pynlpir
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import seaborn as sns; sns.set()
from wordcloud import WordCloud
from imageio import imread
from collections import Counter


web = webdriver.Chrome()
web.maximize_window()
sleep(1)
web.get('https://www.amazon.com/Apple-MacBook-14-inch-8%E2%80%91core-14%E2%80%91core/product-reviews/B09JQSLL92/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews')

sleep(2)
page_count = 0
comment_count = 0

#  --------------getting comments from the link--------------------

file = open("comments.txt", "w")
for i in range(13):
    try:
        sleep(3)
        pageSource = web.page_source
        soup = BeautifulSoup(pageSource, 'html.parser')
        reviews = soup.find('div', id="cm_cr-review_list").find_all('div', class_='a-section celwidget')

        for review in reviews:
            # collect all review contents
            message = review.find('div', class_='a-row a-spacing-small review-data').text
            f_message = message.strip()
            file.write(f_message)
        # click next button
        web.find_element(by=By.CLASS_NAME, value="a-last").click()

    except:
        continue
file.close()
web.close()

# -------------- End getting comments from the link--------------------


font = FontProperties(fname=r'c:\windows\fonts\arial.ttf', size=15)
text_file = open('comments.txt', 'r').read().replace('\n', '')

pynlpir.open()
pynlpir.segment(text_file, pos_names='parent', pos_english=True)

word_list = []
y_list = []

y_list.extend(pynlpir.segment(text_file, pos_names='parent', pos_english=True))

for i in range(len(y_list)):
    y_w = list(y_list[i])
    word_list.append(y_w)

f_words = pd.DataFrame(word_list, columns=["word", "pos"])
f_words.head(25)
f_words.index.size

stopword = open('stopwords_en.txt', encoding='utf-8').read()

for i in range(f_words.shape[0]):
    if f_words.word[i] in stopword:
        f_words.drop(i, inplace=True)
    else:
        pass


wordFormat = pd.DataFrame(f_words["pos"].value_counts(ascending=False))
wordFormat.rename(columns={'pos': 'Frequency'}, inplace=True)

print("\nPart of speech analysis for the review comments\n\n")

# counting POS
print(f"POS {wordFormat.head()}")
print("\n--------------------------------\n")

# counting Frequency
print(f"Word Frequency : {wordFormat['Frequency'].sum()}")
print("\n--------------------------------\n")

# counting percentage of POS
wordFormat['percentage'] = wordFormat['Frequency'] / wordFormat['Frequency'].sum()

print(wordFormat['percentage'])
print("\n--------------------------------\n")




# Extracting words from the file by splitting by " "
wordsCounter = open("comments.txt").read().split()

# Print the top 10 most frequently occurred words in the file, and provide the word frequency for each of them.
word_freq = Counter(wordsCounter)
print("\n\n---------High Frequency words in comments--------\n")
df_wordCount = pd.DataFrame(word_freq.most_common(10))
df_wordCount.columns = ["Words", "Frequency"]
print(df_wordCount)

# # draw wordcloud
myText = ''.join(f_words.word)
myText[:20]
bg_pic = imread('love.png')
wc = WordCloud(mask=bg_pic, max_words=500, max_font_size=50, min_font_size=3, background_color='black', colormap='Reds_r', scale=15.5, contour_color='red', repeat=True)

wc.generate(myText)
plt.imshow(wc)
plt.axis('off')
plt.show()
pynlpir.close()

