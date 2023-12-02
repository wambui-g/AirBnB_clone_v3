#!/usr/bin/python3
"""application api"""
import os
from flask import Flask, jsonify
from flask_cors import CORS

from models import storage
from api.v1.views import app_views


app = Flask(__name__)
"""instance of web application"""
app_host = os.getenv("HBNB_API_HOST", "0.0.0.0")
app_port = int(os.getenv("HBNB_API_PORT", "5000"))
app.register_blueprint(app_views)
app.url_map.strict_slashes = False
CORS(app, resource={'/*': {'origins': app_host}})


@app.teardown_appcontext
def teardown_flask(exception):
    """end event listener"""
    storage.close()


@app.errorhandler(404)
def error_404(error):
    """404 http error"""
    return jsonify(error="Not found"), 404


if __name__ == "__main__":
    app_host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    app_port = int(os.getenv("HBNB_API_PORT", "5000"))
    app.run(
        host=app_host,
        port=app_port,
        threaded=True
    )
