"""API for valid scrabble words"""
# pylint: disable=unused-variable

from flask import Flask
from validator import is_valid_word, is_valid_scrabble_word

app = Flask(__name__)


@app.route("/", methods=["GET"])
def endpoint_index():
    """Landing"""
    return {"message": "Welcome to the Scrabble Dictionary API"}, 200


@app.route("/validate-word-no-reverse/<passed_str>", methods=["GET"])
def endpoint_validate_word_no_reverse(passed_str: str):
    """Check a word is a valid scrabble word, not checking the reverse."""
    if not is_valid_word(passed_str):
        return {
            "error": "Invalid input",
            "message": "Words should only contain alphabetic characters."
        }, 400
    result = is_valid_scrabble_word(passed_str, check_reverse=False)
    return {
        "word": passed_str,
        "validity": result,
    }, 200


@app.route("/validate-word-reverse/<passed_str>", methods=["GET"])
def endpoint_validate_word_reverse(passed_str: str):
    """Check a word is a valid scrabble word, checking the reverse."""
    if not is_valid_word(passed_str):
        return {
            "error": "Invalid input",
            "message": "Words should only contain alphabetic characters."
        }, 400
    result = is_valid_scrabble_word(passed_str, check_reverse=True)
    return {
        "word": passed_str,
        "validity": result,
    }, 200


# if __name__ == "__main__":
#     app.config['TESTING'] = True
#     app.config['DEBUG'] = True
#     app.run(debug=True, host="0.0.0.0", port=5000)
