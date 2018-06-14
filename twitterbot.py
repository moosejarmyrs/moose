import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import datetime
 
consumer_key = 'LoUcUBvcgiho5cGzZ6kbCecQv'
consumer_secret = 'Ep8g1BK2JVqcAuZ7Mu3PpFVDATgSBiouplbnQHPrsAeN3ol4tj'
access_token = '731173585323196416-1zCc7CYv8gYHe2fkSrOIN5XzCXGPrhV'
access_secret = 'I3Txklu19X6RLOp03AgUUguGyOFsx058EuQnGm3ap4QKB'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
 
api = tweepy.API(auth)

class Listener(StreamListener):
	def on_data(self, data):
		try:
			with open("tweets.json", "a+") as f:
				print("Tweet recieved @ " + str(datetime.datetime.now()) + "\n https://twitter.com/anyuser/status/" + str(jsoned_data["id"]) + ".")
				f.write(data)
				jsoned_data = json.loads(data)
				api.send_direct_message(731173585323196416, text=str("Tweet recieved @ " + str(datetime.datetime.now()) + "\n https://twitter.com/anyuser/status/" + str(jsoned_data["id"]) + "."))
				return True
		except BaseException as e:
			print("Error on_data: %s" %str(e))
			api.send_direct_message(731173585323196416, text=str("Bot Down @ " + str(datetime.datetime.now()) + ", ERROR: " + str(e)))
		return True
	def on_error(self, status):
		print(status)
		api.send_direct_message(731173585323196416, text=str("Bot Down @ " + str(datetime.datetime.now()) + ", STATUS: " + str(status)))
		return True

print("Bot started @: " + str(datetime.datetime.now()))
api.send_direct_message(731173585323196416, text=str("Bot started @: " + str(datetime.datetime.now())))
twitter_stream = Stream(auth, Listener())
twitter_stream.filter(follow=["768503362505547776"])
#Sammie: 768503362505547776
#RealActualLava: 731173585323196416
#Beter_Barker69: 951063076115238914
input()
