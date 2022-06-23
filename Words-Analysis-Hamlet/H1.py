import string
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# reading the file
with open('hamlet.txt') as f:
    lines = [line.rstrip() for line in f]

# removing punctuation
s = [sent.translate(str.maketrans('', '', string.punctuation)).split() for sent in lines if sent != '']
words = [sent for sentences in s for sent in sentences]   # collecting all the words
words[:5]


# frequency of item in a list

word_freq = Counter(words)
top_word_freq = word_freq.most_common(20)

top_words = [word[0] for word in top_word_freq]   # all the top frequent words
freq = [word[1] for word in top_word_freq]        # all the frequencies

# max freq in red color in bar plot
bar_plot = plt.bar(top_words, freq)
plt.xticks(rotation = 45);


comment_words = ''    # creating a string of all the words
for tokens in words:
    comment_words += "".join(tokens)+" "

word_cloud = WordCloud(collocations = False, background_color = 'white').generate(comment_words)
# Display the generated Word Cloud
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.show()

