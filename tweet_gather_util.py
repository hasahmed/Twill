import os
import tweepy
import pickle_util as pu

def _get_initilized_tweepy_api():
    consumer_key = "2z8RwVlzdsn2sfJAqVH9LGMVQ"
    consumer_secret = "Q7A7F8R7lcgYZ28fVa2Jqz3eE6zG7dQEl6VtGE5EVWt52DWoEA"
    access_token = "562147599-ue7YHrK4VpWqcv2TA4fSv5huGbws9sZMwrZVJzL5"
    access_token_secret = "AgHMoZn50tFRYeUzWYbOiaGgK7r27hCwnaPsQXp2tldI9"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


class TweetGatherer():
    _storage_directory = "pickledtweets"
    _storage_extension = ".pickle"
    def __init__(self):
        self.api = _get_initilized_tweepy_api()


    '''_get_storage_string(self, username): returns a string representing the directory, filename and extension for a given username'''
    def _get_storeage_string(self, username):
        import os
        return os.path.join(TweetGatherer._storage_directory, username + TweetGatherer._storage_extension)

    # get_tweets_from_disk takes a screen_name as a string and returns list containing every tweet from that person.
    # NOTE** this is sloooooooowwww
    def get_all_tweets_force(self, username):
        alltweets = []
        # make initial request for most recent tweets (200 is the maximum allowed count)
        new_tweets = self.api.user_timeline(screen_name=username, count=200)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # save the id of the oldest tweet minus one
        oldest = alltweets[-1].id - 1
        # keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:
            print("getting tweets before %s" % (oldest))

            # all subsiquent requests use the max_id param to prevent duplicates
            new_tweets = self.api.user_timeline(screen_name=username, count=200, max_id=oldest)

            # save most recent tweets
            alltweets.extend(new_tweets)

            # update the id of the oldest tweet sub 1
            oldest = alltweets[-1].id - 1

            print("...%s tweets downloaded" % (len(alltweets)))

        outtweets = []
        for tweet in alltweets:
            outtweets.append(tweet.text)

        return outtweets

    '''
    Checks the directory pickledtweets/ for a file called username.pickle, and if one exists
    then it returns true. Else it returns false
    '''
    def is_already_gathered(self, username):
        username = username.lower()
        return os.path.isfile(self._get_storeage_string(username))

    '''loads tweets stored on disk into a set and returns it. If nothing on disk exists throws an error'''
    def get_tweets_from_disk(self, username):
        username = username.lower()
        if self.is_already_gathered(username):
            return pu.read_obj_from_disk(self._get_storeage_string(username))
        else:
            tweet_list = self.get_all_tweets_force(username)
            self.write_tweets_to_disk(username, tweet_list)
            return tweet_list


    def write_tweets_to_disk(self, username, tweet_list):
        username = username.lower()
        pu.write_obj_to_disk(tweet_list, self._get_storeage_string(username))


