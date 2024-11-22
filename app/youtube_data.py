from app import config
from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY, YOUTUBE_API_VERSION, YOUTUBE_API_SERVICE_NAME

# Connect to Youtube API
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_KEY)

def fetch_video_description(video_id):
    """Fetch the description of a YouTube video."""
    request = youtube.videos().list(part="snippet", id=video_id)
    response = request.execute()
    
    if "items" in response and len(response["items"]) > 0:
        return response["items"][0]["snippet"]["description"]
    else:
        return "No description found."
    
def get_video_comments(video_id, max_comments=50):
    """ Get comments from a Youtube video by 'video_id' using Youtube Data API."""
    comments = []
    try:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=max_comments,
            textFormat="plainText"
        )
        response = request.execute()

        for item in response.get("items", []):
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

        return comments
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
