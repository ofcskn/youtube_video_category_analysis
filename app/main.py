from graph import plot_sentiment_density
from youtube_data import fetch_video_description, get_video_comments
from config import VIDEO_ID
from nlp_analysis import analyze_sentiment, analyze_sentiment_of_comments, extract_keywords, analyze_keywords_by_language
import json

def main():
    # Fetch video description
    description = fetch_video_description(VIDEO_ID)
    comments = get_video_comments(VIDEO_ID, 20)

    # Perform sentiment analysis
    sentiment = analyze_sentiment(description)
    print("Sentiment Analysis:", sentiment)

    # Extract keywords
    keywords = extract_keywords(description)
    print("Keywords:", keywords)

    # Analyze the keywords of the video
    result = analyze_keywords_by_language(description)
    print("Keyword Analysis (Word, Frequency):")
    print(result)

    # Analyze sentiment of the comments in the video
    sentiment_of_comments = analyze_sentiment_of_comments(comments)
    print("Comment Sentiment Analysis:")
    plot_sentiment_density(sentiment_of_comments)

if __name__ == "__main__":
    main()
