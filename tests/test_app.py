import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_hello_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, IFIAG DevOps Students!" in response.data

def test_status_route():
    client = app.test_client()
    response = client.get('/status')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'ok'
