#!/usr/bin/env python3

from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class template for handling API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the path requires authentication.
        Returns True if path is None or excluded_paths is None or empty
        Returns False if path is in excluded_paths.
        be aware that path may be in shape -> (/endpoint) or (/endpoint/)
        """
        if not path or not excluded_paths:
            return True
        else:
            cur_path = ''.join(path.split('/'))
            ex_paths = [''.join(path.split('/')) for path in excluded_paths]
            if cur_path in ex_paths:
                return False
        return True

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
