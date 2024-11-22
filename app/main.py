from youtube_data import fetch_video_description
from config import VIDEO_ID
from nlp_analysis import analyze_sentiment, extract_keywords, analyze_keywords_by_language

def main():
    # Fetch video description
    description = fetch_video_description(VIDEO_ID)

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

if __name__ == "__main__":
    main()
