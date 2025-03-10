'''APP: API for valid scrabble words'''
# pylint: disable=unused-variable

from flask import Flask
from flask_cors import CORS
from validator import is_valid_word, is_scrabble_word


app = Flask(__name__)
CORS(app, resources={
     r"/*": {"origins": ["https://josephsasaki.github.io", "http://127.0.0.1:5500"]}})


@app.route("/", methods=["GET"])
def endpoint_index():
    '''Landing'''
    return {"message": "Welcome to the Scrabble Dictionary API!"}, 200


@app.route("/validate-word/<passed_str>", methods=["GET"])
def endpoint_validate_word(passed_str: str):
    '''First, check the passed string is a valid word (only alphabetic characters), then check
    if it is a scrabble word.'''
    if not is_valid_word(passed_str):
        return {
            "error": "Invalid input",
            "message": "Words should only contain alphabetic characters."
        }, 400
    result = is_scrabble_word(passed_str)
    return {
        "word": passed_str,
        "forwards": result[0],
        "reversed": result[1],
    }, 200
