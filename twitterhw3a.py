# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
import tweepy
owner = "The_Real_NW"
owner_id = "4854852197"
access_token =  "4854852197-8jZvoSQi6f7gl8U6w3BLrra3k2mCcCvVF0ssp27"
access_token_secret = "e232GRiCiMXz4BrKFFTXWyUT4eDzTeh4SvBmYqGEPGjiN"
consumer_key = "HMDEZrAd2HZaNmIypzJohbkCT"
consumer_secret = "EaqKH4HWP9749QAEQ6wIspK1awlKYYcKTzeeqPIdf3afZEra23"
print("""No output necessary although you 
  can print out a success/failure message if you want to.""")

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "HMDEZrAd2HZaNmIypzJohbkCT",
    "consumer_secret"     : "EaqKH4HWP9749QAEQ6wIspK1awlKYYcKTzeeqPIdf3afZEra23",
    "access_token"        : "4854852197-8jZvoSQi6f7gl8U6w3BLrra3k2mCcCvVF0ssp27",
    "access_token_secret" : "e232GRiCiMXz4BrKFFTXWyUT4eDzTeh4SvBmYqGEPGjiN" 
    }

  api = get_api(cfg)
  tweet = "My name Nate #UMSI-206 #Proj3"
  status = api.update_with_media("206.jpg", tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()