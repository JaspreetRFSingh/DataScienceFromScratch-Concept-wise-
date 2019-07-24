# -*- coding: utf-8 -*-
from twython import Twython
from collections import Counter

# fill these in if you want to use the code
CONSUMER_KEY = "X3PQZ8iGBFvgBFyKSDVTOtd04"
CONSUMER_SECRET = "3kRV0l2Mgc5UDaO4IXyi0CrK0zlrirtPdY3y2vtJGM3lQvoucb"
ACCESS_TOKEN = "1493607384-2fzww6PVQm39ACSRjta3QihljRjOD2TXxiUhPzC"
ACCESS_TOKEN_SECRET = "kgwmzo3j14JTboQhW43ZQrzKU0Ncx3Pa3OivXnNDClPOV"

def call_twitter_search_api():

    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)

    # search for tweets containing the phrase "data science"
    for status in twitter.search(q='"infosys"')["statuses"]:
        user = status["user"]["screen_name"].encode('utf-8')
        text = status["text"].encode('utf-8')
        print(user, ":", text)
        print()


#call_twitter_search_api()

from twython import TwythonStreamer


tweets = []

class MyStreamer(TwythonStreamer):
    def on_success(self, data):

        if data['lang'] == 'en':
            tweets.append(data)

        if len(tweets) >= 100:
            self.disconnect()

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

def call_twitter_streaming_api():
    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET,
                        ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    stream.statuses.filter(track='data')
    for i in range(len(tweets)):
        print(tweets[i]["text"])

#call_twitter_streaming_api()
        
