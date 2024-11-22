from graph import plot_sentiment_density
from youtube_data import fetch_video_description, get_channel_information, get_video_comments
from config import VIDEO_ID, YOUTUBE_CHANNEL_ID
from nlp_analysis import analyze_sentiment, analyze_sentiment_of_comments, extract_keywords, analyze_keywords_by_language
from models.channel import Channel
import json

def main():
    # # Fetch video description
    # description = fetch_video_description(VIDEO_ID)
    # comments = get_video_comments(VIDEO_ID, 20)

    # # Perform sentiment analysis
    # sentiment = analyze_sentiment(description)
    # print("Sentiment Analysis:", sentiment)

    # # Extract keywords
    # keywords = extract_keywords(description)
    # print("Keywords:", keywords)

    # # Analyze the keywords of the video
    # result = analyze_keywords_by_language(description)
    # print("Keyword Analysis (Word, Frequency):")
    # print(result)

    # # Analyze sentiment of the comments in the video
    # sentiment_of_comments = analyze_sentiment_of_comments(comments)
    # print("Comment Sentiment Analysis:")
    # plot_sentiment_density(sentiment_of_comments)
    
    # # Get the channal information
    channel = get_channel_information(YOUTUBE_CHANNEL_ID)
    channel_items = channel["items"][0]
    channel_snippet = channel_items["snippet"]
    channel_statistics = channel_items["statistics"]
    print(channel_statistics)
    try:
        local_channel = Channel(channel_items["id"],channel_snippet["title"], channel_snippet["description"], channel_statistics["subscriberCount"], channel_snippet["publishedAt"], channel_snippet["thumbnails"]["default"]["url"],channel_statistics["viewCount"], channel_statistics["videoCount"])
        local_channel.save()
    except Exception as e:
        print("Error: ", e)
        pass

    pass

if __name__ == "__main__":
    main()
