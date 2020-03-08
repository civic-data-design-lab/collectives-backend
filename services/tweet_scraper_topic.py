from twython import Twython
import json
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

oc_twitter_handle = 'mitsap'

# Load credentials from json file
with open("../twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
twitter = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Get the followers list
# TO DO cursor returned user IDs
follower_request = twitter.get(endpoint='https://api.twitter.com/1.1/followers/ids.json', params={'screen_name':oc_twitter_handle,'count':5000})
follower_list=follower_request['ids']

# TO DO Check if user name already in database, skip
for index, follower in enumerate(follower_list):
    # TO DO can only query 900 times in 15 minute window. 100,000 times per 24 hours
    # TO DO reduce amount of data stored -- lots of columns we might not need
    returned = twitter.get(endpoint='https://api.twitter.com/1.1/statuses/user_timeline.json', params={'user_id':follower,'count':200, 'exclude_replies':True, 'include_rts':False})
    if (index==0):
        tweets_df = pd.DataFrame(returned)
        tweets_df['user'] = follower
    else:
        temp_df = pd.DataFrame(returned)
        temp_df['user'] = follower
        tweets_df = tweets_df.append(temp_df)

# TFIDF language model
tfidf_vect = TfidfVectorizer(max_df=0.8, min_df=2, stop_words='english')
doc_term_matrix = tfidf_vect.fit_transform(tweets_df['text'].values.astype('U'))

# Pulling out 10 topics
nmf = NMF(n_components=10, random_state=42)
nmf.fit(doc_term_matrix )

# adding topics to list
topic_list = []

for i,topic in enumerate(nmf.components_):
    topic_list.append([tfidf_vect.get_feature_names()[i] for i in topic.argsort()[-10:]])

# TO DO: Push topic list to JSON somewhere w/date

# adding topic values to tweets DF
topic_values = nmf.transform(doc_term_matrix)
tweets_df['Topic'] = topic_values.argmax(axis=1)
# TO DO: Push tweets_df to table 1

# getting frequency of topic usage by twitter user
topic_frequency = tweets_df.groupby(['user','Topic']).size().reset_index().rename(columns={0:'Topic Frequency'})

# Push topic_frequency to table 2