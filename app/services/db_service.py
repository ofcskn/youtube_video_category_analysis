from pymongo import MongoClient
from config import DATABASE_NAME, DATABASE_URL

# The database service's purpose is storing the data of Youtube API to save query quota!
class DBService:
    def __init__(self, uri=DATABASE_URL, db_name=DATABASE_NAME):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.db = None

    def connect(self):
        """Establishes a connection to the MongoDB database."""
        if not self.client:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
        return self.db

    def get_collection(self, collection_name):
        """Gets a MongoDB collection."""
        db = self.connect()
        return db[collection_name]

    def close(self):
        """Closes the MongoDB connection."""
        if self.client:
            self.client.close()
