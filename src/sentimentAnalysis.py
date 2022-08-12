#pip install vaderSentiment

# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# function to print sentiments
# of the sentence.
def sentiment_scores(sentence):
	sid_obj = SentimentIntensityAnalyzer()
	sentiment_dict = sid_obj.polarity_scores(sentence)
	print("Sentence:",sentence)
	print("Sentiment score is ", sentiment_dict['compound'])
	print("Overall sentiment dictionary is : ", sentiment_dict)
    



# Driver code
if __name__ == "__main__" :
	sentiment_scores("study is going on as usual")
	sentiment_scores("I am very sad today.")
