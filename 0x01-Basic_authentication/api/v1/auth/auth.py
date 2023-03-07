#!/usr/bin/env python3
"""
Authentication module
"""


from flask import request
from typing import List, TypeVar


class Auth():
    """
    Authentication class, manages API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        validates path
        """
        invalid_path = f"{path}/"
        if path is None:
            return True
        elif len(excluded_paths) == 0 or excluded_paths is None:
            return True
        elif path in excluded_paths or invalid_path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        validates authorization
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        validates current user
        """
        return None
