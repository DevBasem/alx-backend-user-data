#!/usr/bin/env python3
"""
Flask app for user authentication service.
"""

from flask import Flask, request, jsonify
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/users', methods=['POST'])
def users():
    """Endpoint to register a new user."""

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            user = AUTH.register_user(email, password)
            response_data = {
                "email": user.email,
                "message": "user created"
            }
            return jsonify(response_data), 200
        except ValueError as e:
            return jsonify({"message": "email already registered"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
