'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from wordcloud import WordCloud
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Import your Twitter data, json library, and textblob library.
# # Create a list for polarity and subjectivity.
# polarityList = []
# subjectivityList = []
# # For each tweet, make a textblob from the text.
# for eachTweet in tweetData:
#     tweetBlob = TextBlob(eachTweet["text"])
# # Store each tweet's polarity and subjectivity in the list.
#     polarityList.append(tweetBlob.polarity)
#     subjectivityList.append(tweetBlob.subjectivity)
# # Print out the average polarity and subjectivity.
# print('\n' + "Polarity List")
# print(polarityList)
# print('\n' + "subjectivity List")
# print(subjectivityList)
#
# # Create a histogram plot in matplotlib.
# # Give it polarity data and a list of bins.
# plt.hist(polarityList, bins=[-1.1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])
#
# # Set the x and y labels.
# plt.xlabel('Polarities')
# plt.ylabel('# of Tweets')
# plt.title('Histogram of Tweet Polarity')
# # Set the axis to fit your data range.
# plt.axis([-1.1,1.1,0,100])
# plt.grid(true)
# # Show your plot.
# plt.show
# # Create another histogram for subjectivity.// OPTIONAL


# Add `from wordcloud import WordCloud` to the beginning of your file
# Combine all the tweets into one large string.
combinedTweets = ""
for eachTweet2 in tweetData:
    combinedTweets += eachTweet2['text']
# Remember loops and string operators?
# Create a textblob from the combined string.
tweetBlob2 = TextBlob(eachTweet2["text"])

# Generate your own dictionary of `filteredWords[word] = count`
# by looping TextBlob's words list and word_counts dictionary.
wordsToFilter = ["about", "https","http", "www", "com" "org"]
filteredDitionary = dict()

for word in tweetBlob2.words:
    #skip short words that are less the 2 characters long

    if len(word) <= 2:
        continue
        # skip if not a letter
    if not word.isalpha():
        continue
    if word.lower() in wordsToFilter:
            continue;
        # Put all of this into our Dictionary!
    filteredDitionary[word.lower()] = tweetBlob2.word_counts[word.lower()]

# Skip words you don't want in your filtered dictionary.
# Generate a word cloud from the frequencies.
tweetWordCloud = WordCloud().generate_from_frequencies(filteredDitionary)
plt.imshow(tweetWordCloud, interpolation='billinear')
plt.axis("Off")
plt.show()


# Textblob sample:
# tb = TextBlob("You are a brilliant computer scientist.")
# print(tb.polarity)
