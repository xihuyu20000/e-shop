import pytest
from fastapi.testclient import TestClient
from extend import config
from main import app

client = TestClient(app, base_url='http://localhost:8888')

@pytest.fixture(scope='session')
def test_login():
    resp = client.post(config.API_PREFX+'login/', json={'username':'root', 'password':'admin'})
    print(resp)
    assert resp.status_code == 200
