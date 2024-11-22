from services.db_service import DBService

class Channel:
    def __init__(self, name, subscribers, views):
        self.name = name
        self.subscribers = subscribers
        self.views = views
        self.db_service = DBService() 
        self.collection = self.db_service.get_collection("channels")

    def save(self):
        """Saves a channel to the MongoDB database"""
        channel_data = {
            "name": self.name,
            "subscribers": self.subscribers,
            "views": self.views
        }
        result = self.collection.insert_one(channel_data)
        return result.inserted_id