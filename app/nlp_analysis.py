import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

nltk.download("vader_lexicon")

def analyze_sentiment(text):
    """Perform sentiment analysis on the given text."""
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)

def extract_keywords(text, top_n=5):
    """Extract keywords from the text using simple frequency analysis."""
    vectorizer = CountVectorizer(stop_words="english", max_features=top_n)
    X = vectorizer.fit_transform([text])
    return vectorizer.get_feature_names_out()
