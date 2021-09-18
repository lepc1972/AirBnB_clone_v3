#!/usr/bin/python3
"""
    Module REST API Flask App that send json info to front
"""
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
import os

host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': host}})
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """
        Closes the session
    """
    storage.close()


if __name__ == "__main__":
    """
        Entry point app.py
    """
    app.run(host=host, port=int(port), threaded=True)
