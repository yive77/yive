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
			return existing_record 
		return False 

	def store_user(self, register_form):
		email = register_form["email"]
		if self.exists('email', email):
			return False
		user = self.create_user(register_form)
		self.db.users.insert_one(user)

		return user

	def create_user(self, register_form):
		user = {}
		user["last_name"] = register_form.get("last_name").strip()
		user["first_name"] = register_form.get("first_name").strip()
		user["email"] = register_form.get("email").strip()
		user["salt"] = uuid.uuid4().hex 
		user["password_hash"] = self.encrypt_user_pw(user["salt"], register_form["password"])
		return user 


	def encrypt_user_pw(self, salt, password):
		user_password_hash = hmac.new(bytes(salt, 'utf-8'), bytes(password, 'utf-8')).hexdigest()
		return user_password_hash

	def login(self, request_form):
		authenticated, user = False, None 
		email = request_form["email"].strip()
		password = request_form["password"].strip()

		user = self.exists("email", email)
		if user:
			salt = user["salt"]
			password_hash = self.encrypt_user_pw(salt, password)
			if password_hash == user["password_hash"]:
				authenticated = True 
				return authenticated, utility.remove_keys(user, keys=["_id", "salt", "password_hash"])
		return authenticated, user