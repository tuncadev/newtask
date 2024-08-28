
# Order Processing Service

## 🍂 Overview

Welcome to the **Order Processing Service** project! This service is designed to efficiently handle order processing in an e-commerce environment. It features robust order management and real-time notification capabilities, ensuring smooth operations for your platform.

### Key Components:

1. **📦 Order Processing API**: Manages the creation and retrieval of orders, stores data in PostgreSQL, logs changes in MongoDB, and sends notifications via RabbitMQ.
2. **🔔 Notification Service**: Listens for new order notifications in RabbitMQ and broadcasts them to clients using WebSocket.

## 🌟 Features

- **Order Management**:
  - 📝 **Create Orders**: Submit orders via a POST request.
  - 🔍 **Retrieve Orders**: Get order details with a GET request.
  - 💾 **Data Storage**: Uses PostgreSQL for primary storage.
  - 📜 **Change Logging**: Logs order changes in MongoDB.

- **Notification System**:
  - 🚀 **Real-Time Notifications**: Sends notifications via RabbitMQ.
  - 🌐 **WebSocket Broadcasting**: Delivers updates to connected clients.

## ⚙️ Technologies Used

- **⚡ FastAPI**: Powers the asynchronous web APIs.
- **🐘 PostgreSQL**: Serves as the relational database for storing order data.
- **🍃 MongoDB**: Logs order history in a NoSQL format.
- **🐰 RabbitMQ**: Manages message brokering for notifications.
- **🔌 WebSockets**: Provides real-time communication to clients.
- **📦 SQLAlchemy**: Handles ORM and database interactions.
- **🛠️ Pydantic**: Validates data models.
- **🌐 HTTPX**: Manages async HTTP requests in tests.
- **🧪 pytest**: Runs unit tests.
- **🔐 dotenv**: Manages environment variables.

## 🛠️ Installation

### Prerequisites

- 🐍 Python 3.8+
- 🐘 PostgreSQL
- 🍃 MongoDB
- 🐰 RabbitMQ

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/order-processing-service.git
   cd order-processing-service
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root of the project and add the following content:
     ```bash
     DATABASE_USER=order_user
     DATABASE_PASSWORD=your_password
     DATABASE_HOST=localhost
     DATABASE_NAME=order_service_db
     DATABASE_PORT=5432
     ```

5. **Run the application**:
   ```bash
   uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
   ```

6. **Set up the databases**:
   - Make sure PostgreSQL and MongoDB are running.
   - Ensure RabbitMQ is running and configured properly.

## 🚀 Usage

### API Endpoints

- **Create an Order**: `POST /orders/`
  - Request Body:
    ```json
    {
        "product_id": 1,
        "quantity": 2,
        "client_name": "John Doe",
        "client_email": "john.doe@example.com"
    }
    ```

- **Get Order Details**: `GET /orders/{order_id}`
  - Response:
    ```json
    {
        "id": 1,
        "product_id": 1,
        "quantity": 2,
        "client_name": "John Doe",
        "client_email": "john.doe@example.com",
        "status": "Pending",
        "total_price": 200.0
    }
    ```

### WebSocket Notifications

- **Connect to WebSocket**: `ws://127.0.0.1:8001/ws/notifications`
  - Clients will receive notifications when new orders are created.

## 🧪 Testing

### Running Tests

1. **Run the tests**:
   ```bash
   pytest -vv
   ```

2. **Test Coverage**:
   - The project includes tests for:
     - Order creation and retrieval.
     - WebSocket notifications.