import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import tensorflow as tf
import tensorflow_hub as hub

# Importing the Dataset

df = pd.read_csv('C:/Users/pc/Desktop/AI and ML/ML/Datasets/Tweets.csv.')
print(df.head(10))

# First of all let's drop the columns which we don't required

waste_col = ['tweet_id', 'airline_sentiment_confidence',
             'negativereason', 'negativereason_confidence', 'airline',
             'airline_sentiment_gold', 'airline_sentiment', 'negativereason_gold',
             'retweet_count', 'tweet_coord', 'tweet_created',
             'tweet_location', 'user_timezone']

df = df.drop(waste_col, axis=1)
print(df.columns)

## Checking for empty value cells.

null_cols = df.isna().sum()
null_cols, df.shape

df = df.dropna()
print(df)
print(df.shape)

import nltk
from nltk.corpus import stopwords
from spacy.lang.en.stop_words import STOP_WORDS
from wordcloud import WordCloud

# Create stopword list:
STOP_WORDS.add('otter')
stopwords = set(list(STOP_WORDS) + list(stopwords.words()))
stopwords.update(["br", "href", 'https'])
stopwords.update(stopwords)
text = " ".join(desc for desc in df.text)
wordcloud = WordCloud(stopwords=stopwords).generate(textt)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('wordcloud11.png')
plt.show()
