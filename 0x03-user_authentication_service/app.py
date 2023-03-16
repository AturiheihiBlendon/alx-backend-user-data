#!/usr/bin/env python3
"""
Basic flask app module
"""

from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """
    returns the home page
    """
    message = {"message": "Bienvenue"}
    return jsonify(message)


@app.route("/users", methods=['POST'], strict_slashes=False)
def register():
    """
    A method to register users
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login():
    """
    Handles login sessions
    """
    email = request.form.get('email')
    password = request.form.get('password')

    valid_user_login = AUTH.valid_login(email, password)

    if valid_user_login:
        session_id = AUTH.create_session(email)
        response = jsonify({"email": f"{email}", "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response

    abort(401)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
