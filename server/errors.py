no_auth_error = {
	"error": True,
	"message": "Not Authorized"
}

no_auth_required_error = {
	"error": True,
	"message": "You must not be logged in to access this resource"
}


def create_incomplete_form_error(form_elments):
	return {
		"error": True,
		"message": "All fields are required",
		"form_elements": form_elments
	}