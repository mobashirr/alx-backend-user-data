#!/usr/bin/env python3
"""
Module of Index Views for API Endpoints.

This module defines various API endpoints to provide the status of the API,
retrieve object statistics, and handle unauthorized or forbidden requests.

Routes:
    - /status: Returns the operational status of the API.
    - /stats: Provides the count of specific objects.
    - /unauthorized: Endpoint that triggers a 401 Unauthorized response.
    - /forbidden: Endpoint that triggers a 403 Forbidden response.
"""

from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """
    GET /api/v1/status
    Provides the status of the API.

    Returns:
        Response (str): JSON response with the API status.
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """
    GET /api/v1/stats
    Provides the count of each object type in the API.

    Returns:
        Response (str): JSON response with counts for each object type.
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized/', strict_slashes=False)
def unauthorized() -> str:
    """
    GET /api/v1/unauthorized
    Triggers an Unauthorized response (401) to simulate unauthorized access.

    Returns:
        Response: 401 HTTP status code response.
    """
    return abort(401)


@app_views.route('/forbidden/', strict_slashes=False)
def forbidden() -> str:
    """
    GET /api/v1/forbidden
    Triggers a Forbidden response (403) to simulate forbidden access.

    Returns:
        Response: 403 HTTP status code response.
    """
    return abort(403)
