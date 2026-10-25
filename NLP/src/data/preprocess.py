import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
 
try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon")
 
analyzer = SentimentIntensityAnalyzer()
 
 
def create_sentiment(text):
 
    score = analyzer.polarity_scores(str(text))["compound"]
 
    if score >= 0.05:
        return "positive"
 
    elif score <= -0.05:
        return "negative"
 
    else:
        return "neutral"