#!/usr/bin/python3
"""blueprint of the API"""
from flask import Blueprint

api_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

import api.v1.viwes.index
