from services.db_service import DBService

class Channel:
    def __init__(self, id, name, description, subscribers, publishedAt, thumbnail, views, videoCount):
        self.id = id
        self.name = name
        self.description = description
        self.subscribers = subscribers
        self.publishedAt = publishedAt
        self.views = views
        self.thumbnail = thumbnail
        self.videoCount = videoCount
        self.db_service = DBService() 
        self.collection = self.db_service.get_collection("channels")

    def save(self):
        """Saves a channel to the MongoDB database"""
        channel_data = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "subscribers": self.subscribers,
            "publishedAt": self.publishedAt,
            "thumbnail": self.thumbnail,
            "views": self.views,
            "videoCount": self.videoCount
        }
        result = self.collection.insert_one(channel_data)
        return result.inserted_id