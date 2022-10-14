import tweepy

class Twitter(object):
  def __init__(self) -> None:
    self.TWITTER_KEY = ""
    self.TWITTER_SECRET = ""
    self.TWITTER_ACCESS_KEY = ""
    self.TWITTER_ACCESS_SECRET = ""

    self.api = self._authenticate_twitter()
  
  def _authenticate_twitter(self):
      """Authenticates WhenItThursday account for Twitter API.
      Args:
          None
      Returns:
          tweepy.API(auth) (obj): Authentication handler for Twitter API.
      """
      auth = tweepy.OAuthHandler(self.TWITTER_KEY, self.TWITTER_SECRET)
      auth.set_access_token(self.TWITTER_ACCESS_KEY, self.TWITTER_ACCESS_SECRET)
      return tweepy.API(auth)
    

if __name__ == "__main__":
  twitter = Twitter()
  chunked_vid = twitter.api.media_upload(filename=r"thurs.mp4", chunked=True)
  twitter.api.update_status(status="Aw yeeeah", media_ids=[chunked_vid.media_id_string])