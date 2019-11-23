from config import Config
from pymongo import MongoClient

class MongoHandler:

	def __init__(self):
		self.mongo_client = MongoClient(Config.mongodb_connstr)
		self.db = self.mongo_client["yive"]

	def store_user(self, username, password):
		pass

