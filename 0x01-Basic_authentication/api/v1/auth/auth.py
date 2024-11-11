#!/usr/bin/env python3

'''
all authintcatin system implemented in this module
'''

from flask import request

class Auth:
    
    def require_auth(self, path: str, excluded_paths: list[str]) -> bool:
        return False
    
    def authorization_header(self, request=None) -> str:
        return None
    
    def current_user(self, request=None):
        return None
