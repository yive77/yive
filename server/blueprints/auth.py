from builtins import Exception, len
from flask import Blueprint, request, render_template, jsonify
from flask_cors import cross_origin
from middleware import *
from errors import *

from mongo_handler import MongoHandler

auth_blueprint = Blueprint('auth_blueprint', __name__, template_folder='templates')


@cross_origin
@auth_blueprint.route("/api/register", methods=["POST"])
@no_auth_required
@form_sanity
def register(*args, **kwargs):
	try:
		no_satisfy = kwargs["no_satisfy"]
		if len(no_satisfy) > 0:
			return jsonify(create_incomplete_form_error(no_satisfy))
		else:
			mongo = MongoHandler()
			user = mongo.store_user(request.form)
			print(user)
			return "success"

	except Exception as e:
		print(str(e))
		return str(e)
		pass

