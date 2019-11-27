from builtins import getattr
import os
import importlib

from config import Config

cwd = os.getcwd()
blueprints_folder = "%s/%s" % (cwd, "blueprints")

# dynamically import all blueprints. #winning
def read_blueprints():
	blueprint_instances = []
	files = os.listdir(blueprints_folder)
	for f in files:
		if f not in Config.exclude_files:
			import_name = f.split(".py")[0]
			# blueprint_instance = importlib.import_module()
			module = importlib.import_module(".%s" % import_name, package="blueprints")
			blueprint_name = "%s_blueprint" % import_name
			blueprint_instance = getattr(module, blueprint_name)
			blueprint_instances.append(blueprint_instance)
	return blueprint_instances


# remove keys from values as we need to
def remove_keys(obj, keys=[]):
	for k in keys:
		del obj[k]
	return obj




