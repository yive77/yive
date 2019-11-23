
class Config:
	"""
		static level class variables for app/cloud configuration.
		shared resources, etc
	"""
	exclude_files = [
		"__pycache__",
		"__init__.py"
	]
	mongodb_connstr = "mongodb+srv://dylan:<winning123>@cluster0-1pnsw.gcp.mongodb.net/test?retryWrites=true&w=majority"


class FlaskConfig:
	DEBUG = True
	SECRET_KEY = '8a8b4c5d890e42728b5ed94cd0dc98e4'
	SESSION_TYPE = 'filesystem'
