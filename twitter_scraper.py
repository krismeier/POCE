import sys
import tweepy

# Create variables for each key, secret, token
consumer_key = 'MyKey'
consumer_secret = 'MySecret'
access_token = 'MyToke'
access_token_secret = 'MyTokenSecret'

# Setup auth variables
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Overwrite StreamListener methods
class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print status.text

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:'
        return True

    def on_timeout(selfself):
        print >> sys.stderr, 'Timeout...'
        return True

# Stream and filter
sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['test1'])
