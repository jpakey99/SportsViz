import tweepy, datetime, json
from NHL import twitter as nhlTwitter
from MLB import twitter as mlbTwitter


def post_tweet(text, images, reply_id=None, index=0):
    with open('cred.json') as json_file:
        creds = json.load(json_file)

    new_api = creds['new_api']
    new_api_secret = creds['new_api_secret']
    new_access_token = creds['new_access_token']
    new_access_secret = creds['new_access_secret']

    # authentication
    auth = tweepy.OAuthHandler(new_api, new_api_secret)
    auth.set_access_token(new_access_token, new_access_secret)
    api = tweepy.API(auth)

    if index >= len(text):
        pass
    else:
        if reply_id is None:
            image_path = images[index]
            media = api.media_upload(image_path)
            original_tweet = api.update_status(status=text[index], media_ids=[media.media_id])
            print('posted')
            post_tweet(text, images, original_tweet.id, index+1)
        else:
            image_path = images[index]
            media = api.media_upload(image_path)
            original_tweet = api.update_status(status=text[index],
                                             media_ids = [media.media_id],
                                             in_reply_to_status_id=reply_id,
                                             auto_populate_reply_metadata=True)
            print('posted')
            post_tweet(text, images, original_tweet.id, index+1)


def nhl():
    text, images = nhlTwitter.create_viz()
    # text, images = create_indiv_viz()
    post_tweet(text, images)


def mlb():
    text, images = mlbTwitter.create_viz()
    post_tweet(text, images)


if __name__ == '__main__':
    mlb()