import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_websocket_notifications():
    with client.websocket_connect("/ws/notifications") as websocket:
        # Create an order, which should trigger a notification
        response = client.post("/orders/", json={
            "product_id": 1,
            "quantity": 2,
            "client_name": "John Doe",
            "client_email": "john.doe@example.com"
        })
        assert response.status_code == 200

        # Receive the notification without async/await since this is a synchronous test client
        message = websocket.receive_text()
        assert "New order created" in message

        # Test WebSocket disconnect
        websocket.close()
