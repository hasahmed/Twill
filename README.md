# Twill
## The Twitter Utility
This is a probject that attempts to make doing high-level twitter things easy.
A typical use case is text-mining.
This project is built on top of tweepy, and has a readily available tweepy instance in the object. `twill.tweepy_api`

If you would prefer to have your credentials stored so you don't need to write them directly into your code every time,
you can store them in ``$HOME/.twitter_auth` in the format
```
consumer_key : your_consumer_key
consumer_secret : your_consumer_secret
access_token : your_access_token
access_token_secret : your_access_token_secret
```
