from services.db_service import DBService

class Video:
    def __init__(self, title, description, date, views, impressions, ctr, likes, channel_id):
        self.title = title
        self.description = description
        self.date = date
        self.views = views
        self.impressions = impressions
        self.ctr = ctr
        self.likes = likes
        self.channel_id = channel_id
        self.db_service = DBService() 
        self.collection = self.db_service.get_collection("videos")

    def save(self):
        """Saves a video to the MongoDB database"""
        video_data = {
            "title": self.title,
            "description": self.description,
            "date": self.date,
            "views": self.views,
            "impressions": self.impressions,
            "ctr": self.ctr,
            "likes": self.likes,
            "channel_id": self.channel_id
        }
        result = self.collection.insert_one(video_data)
        return result.inserted_id
