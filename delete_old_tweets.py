from datetime import datetime, timedelta, timezone
import time
import json
import os

from TwitterAPI import TwitterAPI


api = TwitterAPI(
    consumer_key=os.environ['TWITTER_APP_KEY'],
    consumer_secret=os.environ['TWITTER_APP_SECRET'],
    access_token_key=os.environ['ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
)


def tweet_created_epoch(t):
    return time.mktime(time.strptime(t['tweet']['created_at'], '%a %b %d %H:%M:%S %z %Y'))


def tweet_datetime(t):
    return datetime.strptime(t['tweet']['created_at'], '%a %b %d %H:%M:%S %z %Y')


def delete_after_datetime():
    return datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)


def delete_prior_to_datetime():
    return datetime(2020, 7, 1, 0, 0, 0, tzinfo=timezone.utc)


with open('./tweet.js') as f:
    data = json.load(f)

tweets_oldest_first = sorted(data, key=tweet_created_epoch)
tweets_to_delete = []
for tweet in tweets_oldest_first:
    tweet_created_at = tweet_datetime(tweet)
    if delete_prior_to_datetime() > tweet_created_at > delete_after_datetime():
        tweets_to_delete.append(tweet)

print('Found {} tweets to delete'.format(len(tweets_to_delete)))
print('Earliest tweet is from {}, ID: {}'.format(tweets_to_delete[0]['tweet']['created_at'], tweets_to_delete[0]['tweet']['id_str']))
print('Most recent tweet is from {}, ID: {}'.format(tweets_to_delete[-1]['tweet']['created_at'], tweets_to_delete[-1]['tweet']['id_str']))

# for tweet in tweets_to_delete:
#     print('Deleting tweet {}'.format(tweet['tweet']['id_str']))
#     r = api.request('statuses/destroy/:{}'.format(tweet['tweet']['id_str']))
#     print('Response: {}'.format(r.status_code))
