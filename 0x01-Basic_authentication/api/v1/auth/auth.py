#!/usr/bin/env python3

from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class template for handling API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the path requires authentication.
        Currently returns False as default behavior.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the request.
        Currently returns None as default behavior.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user based on the request.
        Currently returns None as default behavior.
        """
        return None

