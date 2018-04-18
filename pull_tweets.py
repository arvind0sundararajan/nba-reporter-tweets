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

# Create an Api instance.
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)


"Prints all arguments, each separated by a newline."
def print_stuff(*args):
	for arg in args:
		print(arg)
	print("\n")



"Returns a list of tweets liked by user specified by user_name."
def get_liked_tweets(user_handle):
	return api.GetFavorites(screen_name=user_handle)


"Get tweets retweeted by user specified by user_screen_name."
def get_retweeted_tweets(user_handle):
	return 


"Get users who like specified tweet."
def get_users_who_like_tweet(tweet):
	return


"Get users who retweeted specified tweet."
def get_users_who_retweeted_tweet(tweet):
	return


"Get tweets from user given user_handle."
def get_tweets(user_handle):
	return



if __name__ == '__main__':

	woj_favorites = get_liked_tweets("wojespn")
	tweet_number = 1
	for liked_tweet in woj_favorites:
		print_stuff(tweet_number, liked_tweet.user.name, liked_tweet.created_at, liked_tweet.text)
		tweet_number += 1
