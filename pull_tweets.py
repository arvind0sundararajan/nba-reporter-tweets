#!/usr/bin/env python

# Copyright 2016 The Python-Twitter Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ------------------------------------------------------------------------
# Change History
# 2010-10-01
#   Initial commit by @jsteiner207
#
# 2014-12-29
#   PEP8 update by @radzhome
#
# 2016-05-07
#   Update for Python3 by @jeremylow
#

from __future__ import print_function
import twitter
from secret import *


class TwitterApiWrapper:

	def __init__(self):
		# Create an Api instance.
		self.api = twitter.Api(consumer_key=CONSUMER_KEY,
		                  consumer_secret=CONSUMER_SECRET,
		                  access_token_key=ACCESS_TOKEN,
		                  access_token_secret=ACCESS_TOKEN_SECRET)


	"Returns a list of tweets liked by user specified by user_name."
	def get_liked_tweets(self, user_handle):
		return self.api.GetFavorites(screen_name=user_handle)


	"Get up to 100 retweets of tweet."
	def get_retweeted_tweets(self, tweet):
		return self.api.GetRetweets(tweet.id)



	"Get num_retweeters users who retweeted specified tweet (tweet object)."
	def get_users_who_retweeted_tweet(self, tweet, num_retweeters):
		return self.api.GetRetweeters(tweet.id, count=num_retweeters)


	"Get tweets from user given user_handle."
	def get_tweets(self, user_handle):
		return self.api.GetUserTimeline(self, screen_name=user_handle)


	"Get list of followers (twitter.User instances) for user_handle."
	def get_followers(self, user_handle):
		return self.api.GetFollowers(screen_name=user_handle)





"Prints all arguments, each separated by a newline."
def print_stuff(*args):
	for arg in args:
		print(arg)


INITIAL_STATES = ["wojespn",
	"zachlowe_nba",
	"WindhorstESPN",
	"ShamsCharania",
	"daldridgetnt",
	"ChrisBHaynes",
	"TheSteinLine",
	"Rachel__Nichols",
	"ChrisMannixYS",
	"MarcJSpearsESPN",
	"ramonashelburne"	
]


if __name__ == '__main__':

	taw = TwitterApiWrapper()

	"""
	for reporter_handle in INITIAL_STATES:
		temp_followers = taw.get_followers(reporter_handle)
		print("{}: {}".format(reporter_handle, len(temp_followers)))
	"""
	temp_followers = taw.get_followers(INITIAL_STATES[0])
	print("{}: {}".format(INITIAL_STATES[0], len(temp_followers)))

