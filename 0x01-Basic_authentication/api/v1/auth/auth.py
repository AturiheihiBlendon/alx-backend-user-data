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
        return False

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
