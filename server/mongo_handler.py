from config import Config
from pymongo import MongoClient
import uuid 
import hmac 
import utility 

class MongoHandler:

	def __init__(self):
		self.mongo_client = MongoClient(Config.mongodb_connstr)
		self.db = self.mongo_client["yive"]

	def exists(self, key, value):
		existing_record = self.db.users.find_one({key: value})
		if existing_record:
			return True 
		return False 

	def store_user(self, register_form):
		email = register_form["email"]
		if self.exists('email', email):
			return False
		user = self.create_user(register_form)
		self.db.users.insert_one(user)

		# we will be sending this user obj to the client, so let's make sure we remove any confidential data
		return utility.remove_keys(user, keys=["_id", "password_hash", "salt"])

	def create_user(self, register_form):
		user = {}
		user["last_name"] = register_form.get("last_name")
		user["first_name"] = register_form.get("first_name")
		user["email"] = register_form.get("email")
		user["password_hash"], user["salt"] = self.encrypt_user_pw(register_form["password"])
		return user 



	def encrypt_user_pw(self, password):
		user_salt = uuid.uuid4().hex 
		user_password_hash = hmac.new(bytes(user_salt, 'utf-8'), bytes(password, 'utf-8')).hexdigest()
		return (user_password_hash, user_salt)