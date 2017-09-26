import tweepy, json
from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)  # create an API object


class MyStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        #print(status.text)
        print(data)

        twt = json.loads(data)

        filename = "/Users/foster/Documents/Dartmouth/17F/CS98/hack-a-thing-2-caremorebot/carebar.gif"
        #print(status.id)

        # old_id = status.id

        print(twt['id'])

        user = "@" + str(twt['user']['screen_name'])
        msg = 'Hey ' + user + ', did you mean "I couldn\'t care less"?'

        # matches = ['I could care less', 'could care less', 'I really could care less']

        txt = 'I could care less'
        print(twt['text'])

        print(str(twt['retweeted']) + " \n " + str(type(twt['retweeted'])))

        if twt['text'].find(txt) >= 0 and twt['retweeted'] is False:
            if twt['text'].find('RT @') < 0:
                print("tweeting now")
                api.update_with_media(filename, status=msg, in_reply_to_status_id=int(twt['id']))
            else:
                print('caught RT')
