# pylint: disable=unused-variable
'''Test api file'''
import pytest
from api import app


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
