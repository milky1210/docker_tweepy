import tweepy

import config


def shorten_text(txt):
    if len(txt) > 135:
        return txt[:135] + "..."
    return txt


def tweet_img(filename, txt):
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, ATS)
    api = tweepy.API(auth)
    client = tweepy.Client(
        consumer_key=CK, consumer_secret=CS, access_token=AT, access_token_secret=ATS
    )
    media = api.media_upload(filename=filename)
    client.create_tweet(text=shorten_text(txt), media_ids=[media.media_id])


def tweet_txt(txt):
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    client = tweepy.Client(
        consumer_key=CK, consumer_secret=CS, access_token=AT, access_token_secret=ATS
    )

    client.create_tweet(text=shorten_text(txt))


if __name__ == "__main__":
    pass
    # 検証用スクリプト
    # tweet_txt('tweepyからこんにちは')
