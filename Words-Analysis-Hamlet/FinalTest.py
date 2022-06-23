from collections import Counter
import random
from nltk.util import ngrams
import pandas as pd

# Extracting words from the file by splitting by " "
wordsCounter = open("hamlet.txt").read().split()

# Print the top 10 most frequently occurred words in the file, and provide the word frequency for each of them.
word_freq = Counter(wordsCounter)
print("\n---------High frequency words--------\n")
df_wordCount = pd.DataFrame(word_freq.most_common(10))
df_wordCount.columns = ["Words", "Frequency"]
print(df_wordCount)



# Randomly print 5 words with frequency = 2
print("\n---------Randomly print 5 words with frequency = 2--------\n")
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
print("\n---------10 most frequently occurred bigram words(POS)--------\n")
n_gram = 2
bigram = Counter(ngrams(wordsCounter, n_gram)).most_common(10)
df_wordCountPOS = pd.DataFrame(bigram)
df_wordCountPOS.columns = ["Words", "Frequency"]
print(df_wordCountPOS)


# Print the top 10 most frequently occurred trigram words(three-word triplet) in the file, and provide the word
# frequency for each of them.
print("\n---------10 most frequently occurred trigram words--------\n")
n_gram = 3
trigram = Counter(ngrams(wordsCounter, n_gram)).most_common(10)
df_wordCountThree = pd.DataFrame(trigram)
df_wordCountThree.columns = ["Words", "Frequency"]
print(df_wordCountThree)

