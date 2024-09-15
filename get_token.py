import os
from urllib.parse import parse_qs

import requests
from requests_oauthlib import OAuth1

oauth = OAuth1(os.environ['TWITTER_APP_KEY'], os.environ['TWITTER_APP_SECRET'])
r = requests.post('https://api.twitter.com/oauth/request_token', params={'oauth_callback': 'oob'}, auth=oauth)
credentials = parse_qs(r.text)
request_key = credentials.get('oauth_token')[0]

print('Get the code from https://api.twitter.com/oauth/authorize?{}\n'.format(r.text))
code = input('Enter the code: ')
print()

r = requests.post('https://api.twitter.com/oauth/access_token', params={'oauth_token': request_key, 'oauth_verifier': code})
if r.status_code == 200:
    token_response = parse_qs(r.text)
    token = token_response.get('oauth_token')[0]
    secret = token_response.get('oauth_token_secret')[0]
    screenname = token_response.get('screen_name')[0]

    print('Success! Authenticated as {}.'.format(screenname))
    print('OAuth Token Key: {}'.format(token))
    print('OAuth Token Secret: {}'.format(secret))
else:
    print('Unable to authenticate! Code {}'.format(r.status_code))
