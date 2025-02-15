"""API for valid scrabble words"""
# pylint: disable=unused-variable

from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=["GET"])
def endpoint_index():
    """Landing"""
    return jsonify({"message": "Welcome to the Scrabble Dictionary API"})


if __name__ == "__main__":
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    app.run(debug=True, host="0.0.0.0", port=5000)
