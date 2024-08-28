import pytest
from httpx import AsyncClient
from app.main import app
from httpx import ASGITransport

@pytest.mark.asyncio
async def test_create_order():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        response = await ac.post("/orders/", json={
            "product_id": 1,
            "quantity": 2,
            "client_name": "John Doe",
            "client_email": "john.doe@example.com"
        })
    assert response.status_code == 200
    assert response.json()["product_id"] == 1
    assert response.json()["quantity"] == 2
    assert response.json()["client_name"] == "John Doe"
    assert response.json()["client_email"] == "john.doe@example.com"

@pytest.mark.asyncio
async def test_get_order():
    # First, create an order to retrieve
    async with AsyncClient(app=app, base_url="http://test") as ac:
        create_response = await ac.post("/orders/", json={
            "product_id": 1,
            "quantity": 2,
            "client_name": "John Doe",
            "client_email": "john.doe@example.com"
        })
        order_id = create_response.json()["id"]

        # Now, retrieve the created order
        get_response = await ac.get(f"/orders/{order_id}")
    assert get_response.status_code == 200
    assert get_response.json()["id"] == order_id
    assert get_response.json()["product_id"] == 1
    assert get_response.json()["quantity"] == 2
    assert get_response.json()["client_name"] == "John Doe"
    assert get_response.json()["client_email"] == "john.doe@example.com"
