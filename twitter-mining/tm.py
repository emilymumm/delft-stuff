from twitter import Twitter, OAuth, TwitterStream
import json 

OUTPUT_FILE = "police_rest_api_13-20.json"

ACCESS_TOKEN = '911159906727858176-zmc0r9P3cLH12sP19Jlq7IPO5PlvLoK'
ACCESS_TOKEN_SECRET = 'dXuwSLlktS7xjPimuI5YFR0J3J3Ddr5TcXYEtsH6Ybqu9'
CONSUMER_KEY = 'TlGHzC9IegFhDtY3jrDbQMOEZ'
CONSUMER_SECRET = 'Svtpy68T6eh9HpGrwqzrkEtg2TpY5cSKlCytjoKKrAzoz5f6WB'

t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

# hashtag_list = ['#BLM', '#blacklivesmatter', '#MassIncarceration', 
# 				'#BackTheBlue', '#AllLivesMatter', '#WhiteLivesMatter', 
# 				'#BrownLivesMatter', '#BlueLivesMatter', '#HandsUpDontShoot' 
# 				'#SayHerName', '#sayhisname' '#ICantBreathe', '#ICantBreath']



tweets = t.search.tweets(q = '#BLM')

# tweets = t.search.tweets(q = '%23BLM%2C%20OR%20%23blacklivesmatter%2C%20OR%20%23MassIncarceration%2C%20OR%20%23BackTheBlue%2C%20OR%20%23backthebadge%2C%20OR%20%23AllLivesMatter%2C%20OR%20%23WhiteLivesMatter%2C%20OR%20%23BrownLivesMatter%2C%20OR%20%23BlueLivesMatter%2C%20OR%20%23HandsUpDontShoot%2C%20OR%20%23SayHerName%2C%20OR%20%23sayhisname%2C%20OR%20%23ICantBreathe%2C%20OR%20%23ICantBreath%2C%20OR%20%23Policebrutality%2C%20OR%20%23knowjusticeknowpeace%2C%20OR%20%23thinblueline%2C%20OR%20%23whosestreets%2C%20OR%20%23Stockleyverdict%2C%20OR%20%23stlverdict%2C%20OR%20%23stl%20since%3A2017-09-13%20until%3A2017-09-20')

# tweets = t.search.tweets(q = '@BlueLivesMatter OR @ShaunKing OR @jstines3 OR @SLMPD OR from:@BlueLivesMatter OR from:@ShaunKing OR from:@jstines3 OR from:@SLMPD OR to:@BlueLivesMatter OR to:@ShaunKing OR to:@jstines3 OR to:@SLMPDsince: 2017-10-19 until:2017-10-20', count = 100)


print(len(tweets))
# OR @BlueLivesMatter OR @ShaunKing OR @jstines3 OR @SLMPD OR from:@BlueLivesMatter OR from:@ShaunKing OR from:@jstines3 OR from:@SLMPD OR to:@BlueLivesMatter OR to:@ShaunKing OR to:@jstines3 OR to:@SLMPD'
# since = '2017-10-19' until = 2017-10-20')

# print(tweets)

# print(json.dumps(tweets, indent=2))


# # Opens a file but deletes the contents if the file exists.
# # Every call to write() appends to the end of that empty file.
# # file = open("filename.ext", "w")
# #
# # Opens a file in append mode. When you call "write()" it
# # will add what you write to the end of the file.
# # file = open("filename.ext", "a")

file = open(OUTPUT_FILE,"w")
 
file.write(json.dumps(tweets, indent = 1))
 
file.close() 
