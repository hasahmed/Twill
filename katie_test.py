import tweepy
import inspect
from pprint import pprint
from tweet_gather_util import TweetGatherer

tg = TweetGatherer()

a = tg.api.search("a", geocode="37.781157,-122.398720,100mi", showuser=True)
for tweet in a:
    print(tweet.user.screen_name, end='\n\n')


# print(inspect.getmro(tweepy.models.Status))
