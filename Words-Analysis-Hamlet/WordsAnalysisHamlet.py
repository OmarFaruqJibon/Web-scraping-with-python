import pynlpir as pynlpir
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import seaborn as sns; sns.set()
from wordcloud import WordCloud
from imageio import imread
from nltk.util import ngrams
from collections import Counter

font = FontProperties(fname=r'c:\windows\fonts\arial.ttf', size=15)
text_file = open('hamlet.txt', 'r').read().replace('\n', '')

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
wordsCounter = open("hamlet.txt").read().split()

# Print the top 10 most frequently occurred words in the file, and provide the word frequency for each of them.
word_freq = Counter(wordsCounter)
print("\n\n---------High Frequency words--------\n")
df_wordCount = pd.DataFrame(word_freq.most_common(10))
df_wordCount.columns = ["Words", "Frequency"]
print(df_wordCount)


# Print the top 10 most frequently occurred bigram words(pair of two words) in the file, and provide the word
# frequency for each of them
print("\n\n---------10 most frequently occurred bigram words(POS)--------\n")
n_gram = 2
bigram = Counter(ngrams(wordsCounter, n_gram)).most_common(10)
df_wordCountPOS = pd.DataFrame(bigram)
df_wordCountPOS.columns = ["Words", "Frequency"]
print(df_wordCountPOS)

# Print the top 10 most frequently occurred trigram words(three-word triplet) in the file, and provide the word
# frequency for each of them.
print("\n\n---------10 most frequently occurred trigram words--------\n")
n_gram = 3
trigram = Counter(ngrams(wordsCounter, n_gram)).most_common(10)
df_wordCountThree = pd.DataFrame(trigram)
df_wordCountThree.columns = ["Words", "Frequency"]
print(df_wordCountThree)


# draw chart
plt.subplots(figsize=(7, 5))
wordFormat.iloc[:10]['Frequency'].plot(kind='barh')
plt.yticks(fontproperties=font, size=10)
plt.xlabel('Frequency', fontproperties=font, size=10)
plt.ylabel('POS', fontproperties=font, size=10)
plt.title('POS analysis in comments', fontproperties=font)
plt.show()

# draw wordcloud
myText = ''.join(f_words.word)
myText[:20]
bg_pic = imread('love.png')
wc = WordCloud(mask=bg_pic, max_words=500, max_font_size=50, min_font_size=3, background_color='black', colormap='Reds_r', scale=15.5, contour_color='red', repeat=True)

wc.generate(myText)
plt.imshow(wc)
plt.axis('off')
plt.show()
pynlpir.close()











