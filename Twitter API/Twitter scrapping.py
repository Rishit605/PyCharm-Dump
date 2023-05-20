import configparser
import pandas as pd
import tweepy
from tweepy import OAuthHandler

consumer_key = 'nLJVpW7yVrX5aW4Mo6FUKhW3F'
consumer_secret = 'mMQFzdj23vyI9jC31leAQGusr1lw3TRESVjHx5ozWsnCm2wmDo'
client_id = 'cklvemhzeGI0bFFCT1M2Ym14ejQ6MTpjaQ'
client_secret_id = 'Jk7JH2hJAjjq1rShaziGvXqp5L5589ngTgvCbHX9N3xHLITRIi'

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api']
api_sec_key = config['twitter']['api_sec']

access_tok = config['twitter']['access_token']
access__sec_tok = config['twitter']['access_token_secret']

# print(api_key)

# authentication
auth  = tweepy.OAuthHandler(api_key, api_sec_key)
auth.set_access_token(access_tok, access__sec_tok)
#
api = tweepy.API(auth, wait_on_rate_limit=True,)
public_tweets = api.home_timeline()
print(public_tweets)
# count = 1
#
# for tweet in tweepy.Cursor(api.search_30_day(label="@BNonnecke", query=450, from_date='2020-02-28')).items(50000):
#
#     print(count)
#     count += 1
#
#     try:
#         data = [tweet.created_at, tweet.id, tweet.text, tweet.user._json['screen_name'], tweet.user._json['name'],
#                 tweet.user._json['created_at'], tweet.entities['urls']]
#         data = tuple(data)
#         tweets.append(data)
#
#     except tweepy.TweepError as e:
#         print(e.reason)
#         continue
#
#     except StopIteration:
#         break
#
# df = pd.DataFrame(tweets, columns = ['created_at','tweet_id', 'tweet_text', 'screen_name', 'name', 'account_creation_date', 'urls'])
#
# df.to_csv(path_or_buf = 'C:/Users/pc/Desktop/Code/OP.csv', index=False)