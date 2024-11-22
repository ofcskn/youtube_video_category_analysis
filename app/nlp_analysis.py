import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from langdetect import detect, DetectorFactory
import string

# Set seed for consistent language detection
DetectorFactory.seed = 0

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download("vader_lexicon")
nltk.download('punkt_tab')

# Custom stopwords dictionary for unsupported languages
CUSTOM_STOPWORDS = {
    'tr': [
        've', 'bir', 'bu', 'için', 'ile', 'ama', 'de', 'da', 'ki', 'eğer',
        'gibi', 'diye', 'çok', 'şey', 'mi', 'mı', 'ya', 'o', 'bunu', 'şu',
        'var', 'yok', 'ben', 'sen', 'biz', 'siz', 'onlar', 'ne', 'nasıl',
        'neden', 'her', 'hiç', 'hangi', 'kim', 'kimin', 'şimdi', 'hep'
    ]
}

def analyze_keywords_by_language(description):
    # Handle null or empty descriptions
    if not description or not description.strip():
        return "The description is null or empty. No analysis can be performed."

    try:
        # Detect language
        detected_language = detect(description)
        print(f"Detected Language: {detected_language}")

        # Fetch stopwords for the detected language
        if detected_language in CUSTOM_STOPWORDS:
            stop_words = set(CUSTOM_STOPWORDS[detected_language])
        else:
            # Default to NLTK's stopwords if available
            stop_words = set(stopwords.words(detected_language))

        # Tokenize the text
        tokens = word_tokenize(description.lower())

        # Remove punctuation and stopwords
        tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]

        # Calculate word frequencies
        word_freq = FreqDist(tokens)

        # Sort by intensity (frequency) and return the result
        sorted_keywords = word_freq.most_common()
        return sorted_keywords

    except Exception as e:
        return f"Error during processing: {str(e)}"
    
def analyze_sentiment(text):
    """Perform sentiment analysis on the given text."""
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)

def extract_keywords(text, top_n=5):
    """Extract keywords from the text using simple frequency analysis."""
    vectorizer = CountVectorizer(stop_words="english", max_features=top_n)
    X = vectorizer.fit_transform([text])
    return vectorizer.get_feature_names_out()
