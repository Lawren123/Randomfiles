Import json

tweetFlie = open("tweets_small.jason, r")

tweetData = json.load(tweetFile)

tweetFile.close()

print("Tweet id:", tweetdata[0]["id"])
print("Tweet text:", tweetData[0]["text"])

# how to get all text data with idx more efficent with less tweets
for idx in range(len(tweetData)):
    print ("Tweet text:"+ tweetData[idx]["text"])

# get all data w/o more efficent way with more tweets
for tweet in tweetData:
    # get all tweet text from tweet data
    print("Tweet text: " + tweet["text"])
