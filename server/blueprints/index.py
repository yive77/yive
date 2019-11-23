from flask import Blueprint, render_template

index_blueprint = Blueprint('index_blueprint', __name__, template_folder='templates')


@index_blueprint.route("/", methods=["GET"])
def index():
    return render_template("index.html")
