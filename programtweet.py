import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "zXNEUH8gJUU4uvfvryyhqMNC4",
    "consumer_secret"     : "Bu6waDoifOhLZNu4dca0pfZs5ICJDGPnzj2eE1MjrRCQkW4HL7",
    "access_token"        : "968406008631570432-bQjuJdDuLiO5LN98J11GHGjCxgZ8H94",
    "access_token_secret" : "azbmhDwmIsMjWHPHIDxI2ZknZtecKq7ogOarXAdE16QgS" 
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
