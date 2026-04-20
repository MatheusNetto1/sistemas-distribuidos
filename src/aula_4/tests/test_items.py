from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_criar_item():
    response = client.post("/items", json={
        "nome": "Item Teste",
        "descricao": "Descrição teste"
    })
    assert response.status_code == 200
    assert response.json()["nome"] == "Item Teste"

def test_listar_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_buscar_item():
    create = client.post("/items", json={
        "nome": "Busca",
        "descricao": "Teste"
    })
    item_id = create.json()["id"]

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200

def test_atualizar_item():
    create = client.post("/items", json={
        "nome": "Velho",
        "descricao": "Antigo"
    })
    item_id = create.json()["id"]

    response = client.put(f"/items/{item_id}", json={
        "nome": "Novo",
        "descricao": "Atualizado"
    })

    assert response.status_code == 200
    assert response.json()["nome"] == "Novo"

def test_deletar_item():
    create = client.post("/items", json={
        "nome": "Delete",
        "descricao": "Teste"
    })
    item_id = create.json()["id"]

    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200