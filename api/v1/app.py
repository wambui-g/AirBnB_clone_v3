#!/usr/bin/python3
"""application api"""
import os
from flask import Flask

from models import storage
from api.v1.views import app_views


app = Flask(__name__)
"""instance of web application"""
app_host = os.getenv("HBNB_API_HOST", "0.0.0.0")
app_port = int(os.getenv("HBNB_API+PORT", "5000"))
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_flask(exception):
    """end event listener"""
    storage.close()


if __name__ == "__main__":
    app_host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    app_port = int(os.getenv("HBNB_API_PORT", "5000"))
    app.run(
        host=app_host,
        port=app_port,
        threaded=True
    )
