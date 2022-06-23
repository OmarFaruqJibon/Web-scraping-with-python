# Pandas for file reading/ visualize data
import pandas as pd
import seaborn as sns
import numpy as np
from PIL import Image
#Matplot to visualize data, also Seaborn and pandas do this
import matplotlib.pyplot as plt
# Inline to show images in jupyter notebook
# %matplotlib inline

allData = pd.read_csv('Shakespeare_data.csv', sep=',')


wordcld = pd.Series(allData['PlayerLine'].tolist()).astype(str)

mask = np.array(Image.open("william-shakespeare-black-silhouette.jpg"))
# Most frequent words in the data set. Just because. Using a beautiful wordcloud
from wordcloud import WordCloud
cloud = WordCloud(mask=mask, margin=1,max_font_size=125).generate(' '.join(wordcld.astype(str)))
plt.figure(figsize=(20, 15))
plt.imshow(cloud)
plt.axis('off')
# plt.show()

allData['Player'].replace(np.nan, 'Other', inplace = True)
allData.head(10)
print(allData.head(10))
