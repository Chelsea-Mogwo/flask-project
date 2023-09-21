import pytest
from application.aot_characters import routes
from application import app

def test_show_and_create():
    a = app.test_client()
    response = a.get('/aot_characters/')
    assert response.status_code == 200
    assert b"characters" in response.data

def test_show_character():
    a = app.test_client()
    response1 = a.get('/aot_characters/levi')
    response2 = a.get('/aot_characters/random')
    assert response1.status_code == 200
    assert b"Levi" in response1.data
    assert response2.status_code == 404
    assert b"Opps 404 Not Found: Character doesn\'t exist" in response2.data

def test_update_and_delete():
    pass