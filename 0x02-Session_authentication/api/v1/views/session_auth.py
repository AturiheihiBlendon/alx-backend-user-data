#!/usr/bin/env python3
"""module of session authentication for views"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models.user import User
from typing import Tuple
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login() -> Tuple[str, int]:
    """POST /api/v1/auth_session/login
    Return:
      - JSON representation of a User object.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == '':
        return jsonify({"error": "email missing"}), 400

    if password is None or password == '':
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})

    if users is None or users == []:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

        from api.v1.app import auth
        session_id = auth.create_session(user.id)
        response = jsonify(user.to_json())
        session_name = os.getenv('SESSION_NAME')
        response.set_cookie(session_name, session_id)
        return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """destroys the logout session of the user"""
    from api.v1.app import auth
    destroy_session = auth.destroy_session(request)
    if destroy_session:
        return jsonify({}), 200
    abort(404)
