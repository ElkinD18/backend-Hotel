import pytest
from typing import Any
from app import create_app
from flask_jwt_extended import create_access_token

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['JWT_SECRET_KEY'] = 'SEDE UPS'  
    with app.test_client() as client:
        with app.app_context():
            yield client

@pytest.fixture
def auth_client(client):
    access_token = create_access_token(identity='testuser')
    client.environ_base['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
    return client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.get_json() == {"message": "Welcome to the Hotel Reservation System API"}

def test_hello_world():
    assert "hello" + " " + "world" == "hello world"

def test_users_route(auth_client: Any):
    rv = auth_client.get('/api/users')
    assert rv.status_code == 200

def test_rooms_route(auth_client: Any):
    rv = auth_client.get('/api/rooms')
    assert rv.status_code == 200

def test_accounts_route(auth_client: Any):
    rv = auth_client.get('/api/accounts')
    assert rv.status_code == 200

def test_reservations_route(auth_client: Any):
    rv = auth_client.get('/api/reservations')
    assert rv.status_code == 200

def test_reports_route(auth_client: Any):
    rv = auth_client.get('/api/reports')
    assert rv.status_code == 200

def test_invoices_route(auth_client: Any):
    rv = auth_client.get('/api/invoices')
    assert rv.status_code == 200

def test_financial_records_route(auth_client: Any):
    rv = auth_client.get('/api/financial_records')
    assert rv.status_code == 200

def test_clients_route(auth_client: Any):
    rv = auth_client.get('/api/clients')
    assert rv.status_code == 200