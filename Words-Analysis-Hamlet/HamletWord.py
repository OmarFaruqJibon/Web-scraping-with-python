import pynlpir as pynlpir
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import seaborn as sns; sns.set()
from wordcloud import WordCloud
from imageio import imread
import random
from nltk.util import ngrams
from collections import Counter
import random

font = FontProperties(fname=r'c:\windows\fonts\arial.ttf', size=15)
text = open('hamlet.txt', 'r').read().replace('\n', '')
# print(text[:200])

pynlpir.open()
pynlpir.segment(text, pos_names='parent', pos_english=True)

words = []
year = 1604
year_words = []

year_words.extend(pynlpir.segment(text, pos_names='parent', pos_english=True))

for i in range(len(year_words)):
    ls_year_word = list(year_words[i])
    ls_year_word.append(year)
    words.append(ls_year_word)

# print(words[:20])

df_words = pd.DataFrame(words, columns=["word", "pos", "year"])
df_words.head(25)
df_words.index.size

stopwords = open('stopwords_en.txt', encoding='utf-8').read()

for i in range(df_words.shape[0]):
    if (df_words.word[i] in stopwords):
        df_words.drop(i, inplace=True)
    else:
        pass


df_wordSpechDistribution = pd.DataFrame(df_words["pos"].value_counts(ascending=False))
df_wordSpechDistribution.rename(columns={'pos': 'Frequence'}, inplace=True)

# counting POS
print(df_wordSpechDistribution.head())
print("\n--------------------------------\n")

# counting Frequence
print(f"Word Frequence : {df_wordSpechDistribution['Frequence'].sum()}")
print("\n--------------------------------\n")

# counting percentage of POS
df_wordSpechDistribution['percentage'] = df_wordSpechDistribution['Frequence'] / df_wordSpechDistribution['Frequence'].sum()
print(df_wordSpechDistribution['percentage'])
print("\n--------------------------------\n")



# Extracting words from the file by splitting by " "
wordsCounter = open("hamlet.txt").read().split()

# Print the top 10 most frequently occurred words in the file, and provide the word frequency for each of them.
word_freq = Counter(wordsCounter)
print("\n\n---------High frequency words--------\n")
df_wordCount = pd.DataFrame(word_freq.most_common(10))
df_wordCount.columns = ["Words", "Frequency"]
print(df_wordCount)



# Randomly print 5 words with frequency = 2
print("\n\n---------Randomly print 5 words with frequency = 2--------\n")
list_freq_2 = []
for i in word_freq.items():
    if i.count(2):
        list_freq_2.append(i)
new_list = random.sample(list_freq_2, 5)

df_wordCountTwo = pd.DataFrame(new_list)
df_wordCountTwo.columns = ["Words", "Frequency"]
print(df_wordCountTwo)


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
# plt.subplots(figsize=(7,5))
# df_wordSpechDistribution.iloc[:10]['frequence'].plot(kind='barh')
# plt.yticks(fontproperties=font, size=10)
# plt.xlabel('Frequence', fontproperties=font, size=10)
# plt.ylabel('Part of Speech', fontproperties=font, size=10)
# plt.title('Part of Speech analysis in Hamlet', fontproperties=font)
# plt.show()

# draw wordcloud
myText = ''.join(df_words.word)
myText[:20]
bg_pic = imread('love.png')
wc = WordCloud(mask=bg_pic,
               max_words=500,
               max_font_size=50,
               min_font_size=3,
               background_color='black',
               colormap='Reds_r',
               scale=15.5,
               contour_color='red',
               repeat=True,
               )

# wc = WordCloud(background_color="white",
#                       mask=bg_pic,
#                       contour_width=3,
#                       repeat=True,
#                       min_font_size=3,
#                       contour_color='darkgreen')
wc.generate(myText)
plt.imshow(wc)
plt.axis('off')
plt.show()
pynlpir.close()











