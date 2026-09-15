import os

os.environ["DATABASE_URL"] = "sqlite:///./test_products.db"

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "FastAPI funcionando"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_product():
    response = client.post(
        "/api/products",
        json={
            "name": "Produto de teste",
            "price": 10.50,
            "description": "Produto criado pelo teste",
        },
    )

    assert response.status_code == 201
    product = response.json()
    assert product["name"] == "Produto de teste"
    assert product["price"] == 10.50

    get_response = client.get(f"/api/products/{product['id']}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Produto de teste"


def test_update_product():
    create_response = client.post(
        "/api/products",
        json={"name": "Produto antigo", "price": 5},
    )
    product_id = create_response.json()["id"]

    update_response = client.put(
        f"/api/products/{product_id}",
        json={"name": "Produto atualizado", "price": 8.75},
    )

    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Produto atualizado"
    assert update_response.json()["price"] == 8.75


def test_delete_product():
    create_response = client.post(
        "/api/products",
        json={"name": "Produto para excluir", "price": 3},
    )
    product_id = create_response.json()["id"]

    delete_response = client.delete(f"/api/products/{product_id}")
    assert delete_response.status_code == 200

    get_response = client.get(f"/api/products/{product_id}")
    assert get_response.status_code == 404
