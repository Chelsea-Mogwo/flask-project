import pytest
from . import routes, app

def test_welcome():
    a = app.test_client()
    response = a.get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data