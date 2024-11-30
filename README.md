# Tweet Deleter

Uses your Twitter archive to delete tweets. Useful for moving to more pleasant social networks!

## Usage

- Create a Twitter app at https://developer.x.com
- Download your Twitter archive from https://x.com/settings/download_your_data
- Edit `data/tweets.js` to remove the variable at the top of the file so it is a flat JSON list
- Set up the Python environment with `poetry install`
- Set the following environment variables:
  - `TWITTER_APP_KEY=<app key for your Twitter app>`
  - `TWITTER_APP_SECRET=<app secret for your Twitter app>`
  - `ACCESS_TOKEN_KEY=<access token key for your Twitter profile>`
  - `ACCESS_TOKEN_SECRET=<access token secret for your Twitter profile>`
- Set the date range you want to delete tweets from in `delete_after_datetime` and `delete_prior_to_datetime` in `delete_old_tweets.py`
- Run the script with `delete-old-tweets` to see what will be deleted, uncomment the last block of code to actually delete the tweets
