#!/usr/bin/env python3
"""
Flask app for user authentication service.
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def welcome():
    """Route to return a welcome message."""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
