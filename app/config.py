from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access variables
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
YOUTUBE_API_SERVICE_NAME = os.getenv("YOUTUBE_API_SERVICE_NAME")
YOUTUBE_API_VERSION = os.getenv("YOUTUBE_API_VERSION")
VIDEO_ID = os.getenv("VIDEO_ID")
