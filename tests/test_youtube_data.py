import unittest
from app.youtube_data import fetch_video_description

class TestYoutubeData(unittest.TestCase):
    def test_fetch_video_description(self):
        description = fetch_video_description("example_video_id")
        self.assertIsInstance(description, str)
