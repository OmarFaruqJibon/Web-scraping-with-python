from collections import Counter
import random
from nltk.util import ngrams
import pandas as pd

# Extracting words from the file by splitting by " "
words = open("hamlet.txt").read().split()




# Print the top 10 most frequently occurred words in the file, and provide the word frequency for each of them.
word_freq = Counter(words)
# print(word_freq.most_common(10))
print("High frequency words \n")

df_wordCount = pd.DataFrame(word_freq.most_common(10))
df_wordCount.columns = ["Words", "Frequency"]
print(df_wordCount)

print("\n------- ONE -------\n")




# Randomly print 5 words with frequency =2.
list_freq_2 = []
for i in word_freq.items():
    if i.count(2):
        list_freq_2.append(i)
new_list = random.sample(list_freq_2, 5)
print(new_list)

print("\n------TWO--------\n")





# Print the top 10 most frequently occurred bigram words(pair of two words) in the file, and provide the word
# frequency for each of them
n_gram = 2
bigram = Counter(ngrams(words, n_gram)).most_common(10)
print(bigram)
print("\n-------THREE-------\n")





# Print the top 10 most frequently occurred trigram words(three-word triplet) in the file, and provide the word
# frequency for each of them.
n_gram = 3
trigram = Counter(ngrams(words, n_gram)).most_common(10)
print(trigram)

print("\n--------FOUR ------\n")
