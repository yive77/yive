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

from flask import Flask, redirect, render_template, request, jsonify, url_for

def create_flask_app():
    app = Flask(__name__)    
    app.debug = True
    return app

def setup_app():
    app = create_flask_app()
    return app

app = setup_app()

@app.route("/", methods=["GET"])
def index():
    return "Hello world"














