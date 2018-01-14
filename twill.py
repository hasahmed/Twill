import tweepy
from twill_util import Util


class Twill():
    def __init__(self,
            consumer_key=None,
            consumer_secret=None,
            access_token=None,
            access_token_secret=None):
        '''Initialize the tweepy api'''
        self.util = Util()
        if not consumer_key:
            auth_dict = self.util.get_twitter_auth()
            if not auth_dict:
                raise ValueError("There is a problem with your twitter credentials")
            consumer_key = auth_dict['consumer_key']
            consumer_secret = auth_dict['consumer_secret']
            access_token = auth_dict['access_token']
            access_token_secret = auth_dict['access_token_secret']

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        self.tweepy_api = api
