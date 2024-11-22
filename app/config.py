from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access variables
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
VIDEO_ID = os.getenv("VIDEO_ID")
