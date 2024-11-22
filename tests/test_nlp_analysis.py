import unittest
from app.nlp_analysis import analyze_sentiment, extract_keywords
import numpy as np

class TestNLPAnalysis(unittest.TestCase):
    def test_analyze_sentiment(self):
        sentiment = analyze_sentiment("This is a great video!")
        self.assertIn("compound", sentiment)
        self.assertGreater(sentiment["compound"], 0)

class TestNLPAnalysis(unittest.TestCase):
    def test_extract_keywords(self):
        keywords = extract_keywords("Python is an amazing programming language.", top_n=3)
        self.assertTrue(isinstance(keywords, (list, np.ndarray)))  # Allow list or array
        self.assertEqual(len(keywords), 3)
