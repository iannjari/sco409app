#Import Dependencies
import streamlit as st
import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

st.title('Pre-tweet Sentiment Analyzer')
st.write('Enter tweet below:')

tweet=st.text_area(label='Tweet:')



st.write(tweet)



def sentiment_func(tweet):
    tweet=TextBlob(tweet)
    if tweet.sentiment.polarity > 0:
       return "Sentiment:: Positive :smiley: "
    elif tweet.sentiment.polarity == 0:
       return "Sentiment:: Negative :angry: "
    else:
       return "Sentiment:: Neutral 😐 "

sentiment=sentiment_func(tweet)
st.markdown(sentiment)

def analyze_token_sentiment(tweet):
	analyzer = SentimentIntensityAnalyzer()
	pos_list = []
	neg_list = []
	neu_list = []
	for i in tweet.split():
		res = analyzer.polarity_scores(i)['compound']
		if res > 0.1:
			pos_list.append(i)
			

		elif res <= -0.1:
			neg_list.append(i)
			
		else:
			neu_list.append(i)

	result = {'positives':pos_list,'negatives':neg_list,'neutral':neu_list}
	return result

results=analyze_token_sentiment(tweet)
x = results['positives']
st.header('Positives:')
x
y=results['negatives']
st.header('Negatives:')
y
z=results['neutral']
st.header('Neutrals:')
z

