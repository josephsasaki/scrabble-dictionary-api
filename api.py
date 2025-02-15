"""api.py"""
# pylint: disable=unused-variable

"""API for movies"""
from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def endpoint_index():
    """Landing"""
    return jsonify({"message": "Welcome to the Scrabble Dictionary API"})


if __name__ == "__main__":
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    app.run(debug=True, host="0.0.0.0", port=5000)
