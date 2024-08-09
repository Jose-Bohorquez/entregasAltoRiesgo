# tests/test_app.py

import sys
import os
import pytest

# Añadir el directorio raíz al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # Asegúrate de que la importación sea correcta

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert b'Welcome to the Flask App!' in rv.data  # Asegúrate de que este texto esté en index.html

def test_services(client):
    rv = client.get('/services')
    assert b'Servicios' in rv.data  # Asegúrate de que este texto esté en services.html

def test_contact(client):
    rv = client.get('/contact')
    assert b'Contacto' in rv.data  # Asegúrate de que este texto esté en contact.html
