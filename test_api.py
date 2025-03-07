# pylint: disable=unused-variable
'''Test api file'''
import pytest
from app import app


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
        "message": "Welcome to the Scrabble Dictionary API!"}


def test_invalid_word(client):
    '''Test invalid word returns 400 status code'''
    invalid_word = "$ad32d"
    response = client.get(f"/validate-word/{invalid_word}")
    assert response.status_code == 400


def test_valid_word(client):
    '''Test valid word returns 200 status code with expected return value'''
    valid_word = "hello"
    response = client.get(f"/validate-word/{valid_word}")
    assert response.status_code == 200
    assert response.json["word"] == "hello"
    assert response.json["forwards"] == True
    assert response.json["reversed"] == False
