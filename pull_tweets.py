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

CONSUMER_KEY = 'MbrzeGFih0rv9yuMbnjXl53oW'
CONSUMER_SECRET = 'SbQFvKkDlijxKR0Jufmj6Bbq3l9RjPscJ49Y8LHwSOQGpNUfDc'
ACCESS_TOKEN = '877336882190757890-5p0SVsQ55FSSVG6xIYndrFQpckU9JSy'
ACCESS_TOKEN_SECRET = '3eK153LIS7BOOWTQRRMfbyE99UQMuOMRxxFN8iuopmeGy'


# Create an Api instance.
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

woj_favorites = api.GetFavorites(screen_name='wojespn')

if __name__ == '__main__':
	tweet_number = 1
	for liked_tweet in woj_favorites:
		print("Tweet {}:\n".format(tweet_number))
		print(liked_tweet)
		print("\n")
		tweet_number += 1
