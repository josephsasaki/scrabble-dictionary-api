# pylint: disable=unused-variable
'''Test api file'''
import pytest
from api import app


VALID_WORDS = ["alfa", "bravo", "charlie", "delta", "echo", "foxtrot",
               "golf", "hotel", "inhale", "juliennes", "kilo", "lima", "mike",
               "novemdecillion", "oscillate", "papa", "queen", "romeo", "sierra",
               "tango", "uniform", "victor", "whiskey", "xanthan", "yanked", "zucchetto"]


INVALID_WORDS = ["axxxxx", "bxxxxx", "cxxxxx", "dxxxxx", "exxxxx", "fxxxxx",
                 "gxxxxx", "hxxxxx", "ixxxxx", "jxxxxx", "kxxxxx", "lxxxxx", "mxxxxx",
                 "nxxxxx", "oxxxxx", "pxxxxx", "qxxxxx", "rxxxxx", "sxxxxx",
                 "txxxxx", "uxxxxx", "vxxxx", "wxxxxx", "xxxxxx", "yxxxxx", "zxxxxx"]


VALID_WORDS_REVERSED = [word[::-1] for word in VALID_WORDS]

INVALID_WORDS_REVERSED = [word[::-1] for word in INVALID_WORDS]


@pytest.fixture(name='client')
def test_client():
    '''Test client'''
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_endpoint_index(client):
    '''Test endpoint index'''
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {
        "message": "Welcome to the Scrabble Dictionary API"}


@pytest.mark.parametrize("valid_word", VALID_WORDS)
def test_valid_no_reverse(valid_word, client):
    '''Test valid words return true (when not checking for reverse)'''
    response = client.get(f"/validate-word-no-reverse/{valid_word}")
    assert response.status_code == 200
    assert response.json == {
        "word": valid_word,
        "validity": True}


@pytest.mark.parametrize("invalid_word", INVALID_WORDS)
def test_invalid_no_reverse(invalid_word, client):
    '''Test invalid words return false (when not checking for reverse)'''
    response = client.get(f"/validate-word-no-reverse/{invalid_word}")
    assert response.status_code == 200
    assert response.json == {
        "word": invalid_word,
        "validity": False}


@pytest.mark.parametrize("valid_word_reversed", VALID_WORDS_REVERSED)
def test_valid_reverse(valid_word_reversed, client):
    '''Test valid words return true (when checking for reverse)'''
    response = client.get(f"/validate-word-reverse/{valid_word_reversed}")
    assert response.status_code == 200
    assert response.json == {
        "word": valid_word_reversed,
        "validity": True}


@pytest.mark.parametrize("invalid_word_reversed", INVALID_WORDS_REVERSED)
def test_invalid_reverse(invalid_word_reversed, client):
    '''Test invalid words return false (when checking for reverse)'''
    response = client.get(f"/validate-word-reverse/{invalid_word_reversed}")
    assert response.status_code == 200
    assert response.json == {
        "word": invalid_word_reversed,
        "validity": False}
