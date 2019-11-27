from builtins import vars
from functools import wraps
from flask import session, request, jsonify
from errors import no_auth_error, no_auth_required_error


def is_authenticated(f):
	@wraps(f)
	def is_authenticated_decorator(*args, **kwargs):
		session_token = session.get('session_token', None)
		return f(*args, **kwargs) if session_token else jsonify(no_auth_error)
	return is_authenticated_decorator


def no_auth_required(f):
	@wraps(f)
	def no_auth_required_decorator(*args, **kwargs):
		session_token = session.get('session_token', None)
		return f(*args, **kwargs) if not session_token else jsonify(no_auth_required_error)
	return no_auth_required_decorator


# a function for sanity checking a form in which all form fields are required
def form_sanity(f):
	@wraps(f)
	def form_satisfied_decorator(*args, **kwargs):
		form_elements_not_satisfied = []

		for k in request.form:
			if not request.form[k]:
				form_elements_not_satisfied.append(k)

		kwargs["no_satisfy"] = form_elements_not_satisfied
		return f(*args, **kwargs)

	return form_satisfied_decorator

