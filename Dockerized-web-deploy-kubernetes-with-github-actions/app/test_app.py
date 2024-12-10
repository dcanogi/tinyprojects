# test_app.py
import pytest
from app import app

# El cliente de prueba de Flask
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test para la ruta /api/data
def test_get_data(client):
    response = client.get('/api/data')  # Realiza una solicitud GET
    json_data = response.get_json()  # Obtén los datos JSON de la respuesta
    assert response.status_code == 200  # Verifica que el código de estado sea 200
    assert json_data['message'] == 'Hello from Python!'  # Verifica el mensaje
