#! /usr/bin/python3
import urllib.parse
import requests
import tweepy
import json
import time
from dateutil import parser
from datetime import datetime
# Importing some stuff...

# Defining functions...
def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def rem_time(d):
    s = ''
    s = str(d.year) + '-' + str(d.month) + '-' + str(d.day)
    return s

# YouTube defining stuff
youtube_api_key = ""
caboose_channel_id = "UCnuxAjoYf0cds_5iQA2yM9Q"

# Preparing to send a request
url_params = {
    "part":"snippet",
    "channelId":caboose_channel_id,
    "key":youtube_api_key,
    "order":"date",
    "maxResults":1,
    "type":"video"
}
# Sending a request
req = f"https://www.googleapis.com/youtube/v3/search?{urllib.parse.urlencode(url_params)}"
# Getting what we need
data = requests.get(req).json()
print(data)
time_upload_raw = data["items"][0]["snippet"]["publishedAt"]
video_id = data["items"][0]["id"]["videoId"]
print(video_id)
time_upload = rem_time(parser.parse(time_upload_raw))
how_long_since_caboose = days_between(str(rem_time(datetime.today())), time_upload)

# Defining Twitter API stuff
api_key = ""
api_secret = ""
bearer_token = r""
access_token = ""
access_token_secret = ""

# Setting up Tweepy
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Sending tweet
client.create_tweet(text="It has been, " + str(how_long_since_caboose) + " days since Caboose TV has last uploaded!\nThis may be a day longer than what you thought, we are looking at the days themselves, not the times.\nThe last video uploaded is available here, youtu.be/" + video_id + ".")
print("Done!")



