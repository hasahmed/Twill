# Twill
## The Twitter Utility
This is a project intends to be a collection of high level code for twitter manipulation. If you have written some utilities in python that you would like to add,
please do so.
The overall goal of the utilities provided is to make doing high-level twitter things easy, sucn as collecting every tweet ever from a partiular user, and storing it on disk.
This project is built on top of tweepy (which is a python interface for the Twitter API),
and has a readily available Tweepy instance. The credentials provided in the creation of
the Twill object initilizes this instance and store it as a property. `tw_instance.tweepy_api`

If you would prefer to have your credentials stored so you don't need to write them directly into your code every time,
you can store them in `$HOME/.twitter_auth` in the format
```
consumer_key : your_consumer_key
consumer_secret : your_consumer_secret
access_token : your_access_token
access_token_secret : your_access_token_secret
```
and Twill will parse the credentials at runtime.
If you want to put them in your code, then the twill object's constructor takes your credentials as parameters i.e.
```
from twill import Twill
tw = Twill(
        "your_consumer_key",
        "your_consumer_secrete",
        "your_access_token",
        "your_access_token_secrete"
        )
print(tw.tweepy_api.get_user('twitter'))
```

The above code initializes and uses the underlying tweepy API to get the user associated with the 'twitter' username.
If you have properly configured you `~/.twitter_auth` file the following initilization would also be valid:
```
from twill import Twill
tw = Twill()
print(tw.tweepy_api.get_user('twitter'))
```
