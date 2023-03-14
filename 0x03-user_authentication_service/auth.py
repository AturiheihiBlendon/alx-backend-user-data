#!/usr/bin/env python3
"""
Authentication module
"""


import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes the password and returns bytes
    """
    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_pwd
