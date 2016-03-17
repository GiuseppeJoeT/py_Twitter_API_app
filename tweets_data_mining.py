import json
import pandas as panda
import matplotlib.pyplot as plt
import re

tweets_data_path = 'tweet_mining.json'

# the code that reads our JSON file is into its own function called read_json()


def read_json(file_path):
    results = []
    tweets_file = open(tweets_data_path, 'r')
    for tweet_line in tweets_file:
        try:
            status = json.loads(tweet_line)
            results.append(status)
        except:
            continue
    return results

'''
Next we'll create a function called is_token_in_tweet_text that searches
for and extracts tokens from the tweet text. If it finds a match, it simply
returns True, otherwise False
'''


def is_token_in_tweet_text(token, tweet_text):
    token = token.lower()
    tweet_text = tweet_text.lower()
    match = re.search(token, tweet_text)
    if match:
        return True
    return False

'''
We then add four new columns to our DataFrame; one for each language
keyword use in our original stream search. We populate each column with
tweet text for every tweet that matches our text search tokens.
'''

results = read_json(tweets_data_path)

# create a dataframe
statuses = panda.DataFrame()

# store the text values
statuses['text'] = map(lambda status: status['text'], results)

# store the language values
statuses['lang'] = map(lambda status: status['lang'], results)

# sometimes there may not be a 'place' listed in the tweet, so 'None' if not present
statuses['country'] = map(lambda status: status['place']['country'] if status['place'] != None else None, results)


# New DataFrame columns
statuses['python'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('python', status))

statuses['java'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('java', status))

statuses['c#'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('c#', status))

statuses['ruby'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('ruby', status))


# output the number of tweets where it is True that they contain our keywords

print statuses['python'].value_counts()[True]

print statuses['java'].value_counts()[True]

print statuses['c#'].value_counts()[True]

print statuses['ruby'].value_counts()[True]

