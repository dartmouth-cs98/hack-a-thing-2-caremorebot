import tweepy
from secrets import *
from MyStreamListener import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)  # create an API object

public_tweets = api.home_timeline()

results = api.search("could care less", rpp=1)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=["I could care less"])

filename = "/Users/foster/Documents/Dartmouth/17F/CS98/twitterbot/carebar.gif"

txt = 'I could care less'

#for twt in myStream:
    #if twt.status.find(txt) > 0:
        #msg = 'Did you mean "I couldn\'t care less"?'
        #twt = api.update_with_media(filename, status=msg, in_reply_to_status_id=twt.id)
        #twt = api.update_status(msg, twt.id)





