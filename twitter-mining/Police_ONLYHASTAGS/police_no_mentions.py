import tweepy 
from tweepy import Stream
from tweepy.streaming import StreamListener 
import json
import time
import datetime

# OUTPUT_FILE = "testfile.json"


ACCESS_TOKEN = '777167577311285248-dabAoLEzgIBRv5xUnFfY9GoxePo17a7'
ACCESS_TOKEN_SECRET = 'SB3wRZ30P8Wtc4Jv5eVW07ojPIhX8kI15LdKiOwXydgN8'
CONSUMER_KEY = 'NgiH8oj76HdA1Y1M4uHWPch5d'
CONSUMER_SECRET = '98q6ROCJHdB6f1O1bIMn6V822aeh6wK83NanzJZjAGpzDtQob1'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

class MyListener(StreamListener):

    def __init__(self,api):
        self.tweet_list=[]
        self.count = 1
       
    def on_data(self, data):
        ts = time.time()
        stamp = datetime.datetime.fromtimestamp(ts).strftime('%m%d%H%M')
        file_name = 'no_mentions_police'+stamp+'.json'
        
        try:
            j = json.loads(data)
            self.tweet_list.append(j)
            n=len(self.tweet_list)
  
            if (n%100==0):
            # if n == 2:
                with open(file_name, 'w') as f:
                    json.dump(self.tweet_list,f)
                print("Output File",self.count)
                # print(json.dumps(self.tweet_list, indent=2))
                self.count=self.count+1
                self.tweet_list = []
            return True
        except BaseException as e:
            print("Error on_data:", str(e))
        return True
 
    def on_error(self, status):
        print("Error",status)
        return False

# file = open(OUTPUT_FILE,"w") 
 
# file.write(json.dumps(python_tweets, indent=1))
 
# file.close() 

twitter_stream = Stream(auth, MyListener(auth))

text_list = []
hashtag_list = ['#BLM', '#blacklivesmatter', '#MassIncarceration', 
				'#BackTheBlue', '#backthebadge', '#AllLivesMatter', '#WhiteLivesMatter', 
				'#BrownLivesMatter', '#BlueLivesMatter', '#HandsUpDontShoot', 
				'#SayHerName', '#sayhisname', '#ICantBreathe', '#ICantBreath', 
				'#Policebrutality', '#knowjusticeknowpeace', '#thinblueline', '#whosestreets',
				'#Stockleyverdict']
# mentions_list = ['@BlueLivesMatter', '@ShaunKing', '@jstines3', '@SLMPD']
# from_list = ['from:@BlueLivesMatter', 'from:@ShaunKing', 'from:@jstines3', 'from:@SLMPD']
# to_list = ['to:@BlueLivesMatter', 'to:@ShaunKing', 'to:@jstines3', 'to:@SLMPD']
my_list = []


full_list = text_list
full_list.extend(hashtag_list)
# full_list.extend(mentions_list)
# full_list.extend(from_list)
# full_list.extend(to_list)
full_list.extend(my_list)


twitter_stream.filter(track=full_list)


# file = open(OUTPUT_FILE,"w")

# # json.dumps(python_tweets, indent=1) 
 
# file.write(json.dumps(python_tweets, indent=1))
 
# file.close() 

# print(json.dumps(python_tweets, indent=2))


 
