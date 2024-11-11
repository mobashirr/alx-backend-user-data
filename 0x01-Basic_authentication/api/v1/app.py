#!/usr/bin/env python3
"""
Flask API module setup.

This module sets up the Flask application, including configuration, CORS, 
and authorization handling. It also defines custom error responses and 
registers the app blueprint.

Environment Variables:
- API_HOST: Host for the Flask app, defaults to '0.0.0.0'
- API_PORT: Port for the Flask app, defaults to '5000'
- AUTH_TYPE: Authentication type ('auth' or 'basic_auth')
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize the auth variable based on AUTH_TYPE environment variable
auth = None
AUTH_TYPE = getenv("AUTH_TYPE")

# Dynamically import and assign the appropriate authentication class based on AUTH_TYPE
if AUTH_TYPE == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
elif AUTH_TYPE == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()

@app.before_request
def before_request_handler():
    """
    Request validation before every request.
    
    If an authentication instance (auth) is provided, this handler will:
    - Check if the requested path requires authentication.
    - Validate the presence of an authorization header; if missing, abort with 401.
    - Check for a valid user; if invalid, abort with 403.

    Excluded paths do not require authentication.
    """
    if auth is None:
        return

    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if not auth.require_auth(request.path, excluded_paths):
        # Path does not require authentication, proceed with request
        return
    if auth.authorization_header(request) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)

@app.errorhandler(404)
def not_found(error) -> str:
    """
    Handler for 404 errors (Not Found).
    
    Returns:
        str: JSON response with error message.
    """
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Handler for 401 errors (Unauthorized).
    
    Returns:
        str: JSON response with error message.
    """
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error) -> str:
    """
    Handler for 403 errors (Forbidden).
    
    Returns:
        str: JSON response with error message.
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
