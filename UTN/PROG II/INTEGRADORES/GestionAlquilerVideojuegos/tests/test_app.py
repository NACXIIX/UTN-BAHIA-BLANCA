import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def cliente():
    with app.test_client() as cliente:
        yield cliente

def test_listar_genero(cliente):
    response = cliente.get('/generos')
    assert response.status_code == 200, "Status code esperado: 200"
    assert isinstance(response.json, list), "La response deberia ser una lista"

def test_modificar_genero(cliente):
    recurso_id = 2
    response = cliente.get(f"/generos/{recurso_id}")
    
def test_eliminar_genero(cliente):
    recurso_id = 2
    response = cliente.get(f'/generos/{recurso_id}')
    assert response.status_code == 200, "El id deberia existir antes de ser eliminado. Status code esperado: 200"
    
    response_delete = cliente.delete(f'/generos/{recurso_id}')
    assert response_delete.status_code == 200, "El genero con el id ingresado deberia haber sido eliminado. Status code esperado: 200"
    assert response_delete.json == {"mensaje": "Genero eliminado satisfactoriamente"}
    
    response_get_404 = cliente.get(f'/recursos/{recurso_id}')
    assert response_get_404.status_code == 404, "El recurso eliminado no debería existir. Status code esperado: 404"
    
