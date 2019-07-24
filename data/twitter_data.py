# -*- coding: utf-8 -*-
from twython import Twython
from collections import Counter

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

def call_twitter_search_api():

    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)

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
        
