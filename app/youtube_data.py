from googleapiclient.discovery import build
from app.config import YOUTUBE_API_KEY

def fetch_video_description(video_id):
    """Fetch the description of a YouTube video."""
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = youtube.videos().list(part="snippet", id=video_id)
    response = request.execute()
    
    if "items" in response and len(response["items"]) > 0:
        return response["items"][0]["snippet"]["description"]
    else:
        return "No description found."
