from app.youtube_data import fetch_video_description
from app.nlp_analysis import analyze_sentiment, extract_keywords
from app.config import VIDEO_ID

def main():
    # Fetch video description
    description = fetch_video_description(VIDEO_ID)
    print("Video Description:", description)

    # Perform sentiment analysis
    sentiment = analyze_sentiment(description)
    print("Sentiment Analysis:", sentiment)

    # Extract keywords
    keywords = extract_keywords(description)
    print("Keywords:", keywords)

if __name__ == "__main__":
    main()
