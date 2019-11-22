#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import utility
from flask import Flask
from flask_cors import CORS
from flask_session import Session
from config import Config


# create the app instance
def create_flask_app():
    app = Flask(__name__)
    app.secret_key = Config.secret_key
    app.config["SESSION_TYPE"] = "filesystem"
    CORS(app)
    Session(app)
    return app


# register our dynamically imported blueprints.
def register_blueprints(app):
    app_blueprints = utility.read_blueprints()
    for bp in app_blueprints:
        app.register_blueprint(bp)
    return app


app = register_blueprints(create_flask_app())

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='0.0.0.0', port=8080, debug=True)














