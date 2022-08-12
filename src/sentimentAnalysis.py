# pip install vaderSentiment

# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import simplejson

# function to print sentiments
# of the sentence.


def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    print("")
    print("Sentence:", sentence)
    print("Sentiment score is ", sentiment_dict['compound'])
    print("")


# Driver code
if __name__ == "__main__":
    
    yorumlar = []
    dosya = open('yorumlar.txt', 'r')
    yorumlar = simplejson.load(dosya)
    dosya.close()

    #sentiment_scores(yorumlar[0])
