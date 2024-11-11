#!/usr/bin/env python3
"""
Basic Authentication Module.

This module defines the BasicAuth class, which extends the Auth class
to implement basic authentication mechanisms for the API.
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class inherits from Auth and provides basic authentication.

    Methods:
        extract_base64_authorization_header(authorization_header: str) -> str:
            Extracts the Base64 encoded part of the Authorization header if it is present and valid.
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the Base64 encoded part of the Authorization header.

        If the `authorization_header` contains the prefix "Basic", this method
        will return the encoded credentials part following the "Basic" keyword.
        
        Args:
            authorization_header (str): The Authorization header from the HTTP request.

        Returns:
            str: The Base64 encoded credentials portion of the header if valid.
            None: If the header is missing, invalid, or does not contain "Basic".
        """
        if not authorization_header or \
           not isinstance(authorization_header, str) or \
           not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ')[1]
