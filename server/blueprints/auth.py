from builtins import Exception, len
from flask import Blueprint, request, render_template, jsonify
from flask_cors import cross_origin
from middleware import *
from errors import *
from responses import *
from mongo_handler import MongoHandler

import utility 

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
			return jsonify(success_response) if user else jsonify(email_taken_error)

	except Exception as e:
		print(str(e))
		return str(e)

@cross_origin
@auth_blueprint.route("/api/login", methods=["POST"])
@no_auth_required
@form_sanity
def login(*args, **kwargs):
	try:
		no_satisfy = kwargs["no_satisfy"]
		if len(no_satisfy) > 0:
			return jsonify(create_incomplete_form_error(no_satisfy))
		else:
			mongo = MongoHandler()
			authenticated, user = mongo.login(request.form)
			if authenticated:
				return jsonify(create_success_response("user", user))
			return jsonify(login_error)

	except Exception as e:
		print(str(e))
		return str(e)




