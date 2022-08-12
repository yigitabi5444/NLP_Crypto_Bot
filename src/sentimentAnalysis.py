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
    sid_obj = SentimentIntensityAnalyzer()
    yorumlar = []
    dosya = open('yorumlar.txt', 'r')
    yorumlar = simplejson.load(dosya)
    dosya.close()

    TotalSentiment = 0
    SentimentCount = 0

    for yorum in yorumlar:
        sentiment_dict = sid_obj.polarity_scores(yorum)
        if(sentiment_dict['compound'] != 0):
            print("")
            print("Sentence:", yorum)
            print("Sentiment score is ", sentiment_dict['compound'])
            print("")
            TotalSentiment += sentiment_dict['compound']
            SentimentCount += 1

    print("Data Count:", SentimentCount)
    print("Average Sentiment:", TotalSentiment / SentimentCount)
