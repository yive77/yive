from functools import wraps
from flask import session, request, jsonify
from app_errors import no_auth_error, no_auth_required_error


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

