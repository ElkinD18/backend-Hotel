import pytest
from backend.app import create_app
from typing import Any

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_index(client: Any):
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.get_json() == {"message": "Welcome to the Hotel Reservation System API"}

def test_hello_world():
    assert "hello" + " " + "world" == "hello world"

def test_users_route(client: Any):
    rv = client.get('/api/users')
    assert rv.status_code == 200

def test_rooms_route(client: Any):
    rv = client.get('/api/rooms')
    assert rv.status_code == 200

def test_accounts_route(client: Any):
    rv = client.get('/api/accounts')
    assert rv.status_code == 200

def test_reservations_route(client: Any):
    rv = client.get('/api/reservations')
    assert rv.status_code == 200

def test_reports_route(client: Any):
    rv = client.get('/api/reports')
    assert rv.status_code == 200

def test_invoices_route(client: Any):
    rv = client.get('/api/invoices')
    assert rv.status_code == 200

def test_financial_records_route(client: Any):
    rv = client.get('/api/financial_records')
    assert rv.status_code == 200

def test_clients_route(client: Any):
    rv = client.get('/api/clients')
    assert rv.status_code == 200