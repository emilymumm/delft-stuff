import twitter
import json 

OUTPUT_FILE = "testfile.json"

ACCESS_TOKEN = '777167577311285248-dabAoLEzgIBRv5xUnFfY9GoxePo17a7'
ACCESS_TOKEN_SECRET = 'SB3wRZ30P8Wtc4Jv5eVW07ojPIhX8kI15LdKiOwXydgN8'
CONSUMER_KEY = 'NgiH8oj76HdA1Y1M4uHWPch5d'
CONSUMER_SECRET = '98q6ROCJHdB6f1O1bIMn6V822aeh6wK83NanzJZjAGpzDtQob1'

api = twitter.Api(consumer_key = CONSUMER_KEY,
				consumer_secret = CONSUMER_SECRET,
				access_token_key = ACCESS_TOKEN,
				access_token_secret = ACCESS_TOKEN_SECRET)

tweets = api.GetSearch(raw_query= 'l=&q=stupid%20idiot%20-bad%2C%20-good%20%23DACA%20OR%20%23MAGA%20%40potus%20since%3A2017-09-12%20until%3A2017-09-19', 
	return_json= True)
 

print(tweets)

# print(json.dumps(tweets, indent=2))