import tweepy 
from tweepy import Stream
from tweepy.streaming import StreamListener 
import json
import time
import datetime


ACCESS_TOKEN = '911159906727858176-zmc0r9P3cLH12sP19Jlq7IPO5PlvLoK'
ACCESS_TOKEN_SECRET = 'dXuwSLlktS7xjPimuI5YFR0J3J3Ddr5TcXYEtsH6Ybqu9'
CONSUMER_KEY = 'TlGHzC9IegFhDtY3jrDbQMOEZ'
CONSUMER_SECRET = 'Svtpy68T6eh9HpGrwqzrkEtg2TpY5cSKlCytjoKKrAzoz5f6WB'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

class MyListener(StreamListener):

    def __init__(self,api):
        self.tweet_list=[]
        self.count = 1
       
    def on_data(self, data):
        try:
            j = json.loads(data)
            self.tweet_list.append(j)
            n = len(self.tweet_list)
  
            if (n % 100 == 0):
                ts = time.time()
                stamp = datetime.datetime.fromtimestamp(ts).strftime('%m%d%H%M')
                file_name = '/Users/Emily/data-files/twitter-stream/Abortion_tweets/abortion_twitter' + stamp + '.json'
                with open(file_name, 'w') as f:
                    json.dump(self.tweet_list, f)
                print("Output File", self.count)
                self.count = self.count + 1
                self.tweet_list = []
            return True
        except BaseException as e:
            print("Error on_data:", str(e))
        return True
 
    def on_error(self, status):
        print("Error",status)
        return False

twitter_stream = Stream(auth, MyListener(auth))

text_list = []
hashtag_list = ['abortion', '#abortion', '#unbornlivesmatter', '#prolife', '#prochoice', '#antilife', 
                '#antichoice', '#DefundPP', '#defundplannedparenthood', '#standforlife',
                '#praytoendabortion,', '#marchforlife', '#PlannedParenthood', 
                '#abortionismurder', '#mybodymychoice', '#IStandwithPP', '#standwithPP']
mentions_list = ['@LifeNewsHQ', '@Ppact', '@PPFA', '@Students4LifeHQ']
from_list = ['from:@LifeNewsHQ', 'from:@Ppact', 'from:@PPFA', '@Students4LifeHQ']
to_list = ['to:@LifeNewsHQ', 'to:@Ppact', 'to:@PPFA', '@Students4LifeHQ']
my_list = []

full_list = text_list
full_list.extend(hashtag_list)
full_list.extend(mentions_list)
full_list.extend(from_list)
full_list.extend(to_list)
full_list.extend(my_list)


twitter_stream.filter(track=full_list)




# print(json.dumps(python_tweets, indent=2))


 
