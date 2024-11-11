#!/usr/bin/env python3
"""
Auth module for handling API authentication.

This module defines the Auth class, which serves as a template for
authentication systems in the API, providing methods to check for
authentication requirements, retrieve authorization headers, and
identify the current user.

Classes:
    - Auth: Template for handling API authentication.

"""

from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class template for handling API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the given path requires authentication.

        Args:
            path (str): The requested path.
            excluded_paths (List[str]): A list of paths that do not require authentication.

        Returns:
            bool: True if the path requires authentication, False otherwise.

        Behavior:
            - Returns True if `path` or `excluded_paths` is None or empty.
            - Returns False if `path` is found in `excluded_paths`.
            - Considers paths without or with a trailing slash as equivalent.

        Example:
            If `excluded_paths` contains "/status/" and `path` is "/status",
            this method considers them equivalent and returns False.
        """
        if not path or not excluded_paths:
            return True

        # Normalize paths by removing leading/trailing slashes for comparison
        cur_path = ''.join(path.split('/'))
        ex_paths = [''.join(excluded_path.split('/')) for excluded_path in excluded_paths]

        if cur_path in ex_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the request.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            str: The Authorization header value if present, otherwise None.
        
        Example:
            If the request contains an Authorization header with the value
            "Bearer my_token", this method returns "Bearer my_token".
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user based on the request.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            TypeVar('User'): The current user object. Currently returns None
                             as this is a placeholder for future implementations.
        
        Note:
            This method can be overridden in subclasses to return the user
            instance based on specific authentication logic.
        """
        return None
