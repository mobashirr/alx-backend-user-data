#!/usr/bin/env python3
"""
Basic Authentication Module.

This module defines the BasicAuth class, which extends the Auth class
to implement basic authentication mechanisms for the API.
"""

from auth import Auth
import base64
import binascii


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

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decode the Base64 part of the Authorization header into text
        using base64 decode and utf-8 .

        If the `base64_authorization_header` is not string or is none.
        
        Args:
            base64_authorization_header (str): The Authorization header from the HTTP request.

        Returns:
            str: The decoded Base64 credentials portion of the header if valid.
            None: If the header is missing, invalid, or can't be decoded".
        """
        if not  base64_authorization_header or \
            not isinstance(base64_authorization_header,str):
            return None
        try:
            decoded_val = base64.b64decode(base64_authorization_header).decode('utf-8')
        except binascii.Error as e:
            return None

        return decoded_val
