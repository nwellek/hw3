# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy

owner = "The_Real_NW"
owner_id = "4854852197"
access_token =  "4854852197-8jZvoSQi6f7gl8U6w3BLrra3k2mCcCvVF0ssp27"
access_token_secret = "e232GRiCiMXz4BrKFFTXWyUT4eDzTeh4SvBmYqGEPGjiN"
consumer_key = "HMDEZrAd2HZaNmIypzJohbkCT"
consumer_secret = "EaqKH4HWP9749QAEQ6wIspK1awlKYYcKTzeeqPIdf3afZEra23"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

search = input("What would you like to search for?")
results = api.search(q=search)

for result in results:
    print (result.text)
print("Average subjectivity is")
print("Average polarity is")