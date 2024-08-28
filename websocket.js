const ws = new WebSocket("wss://127.0.0.1:8000/ws/notifications");

ws.onopen = function(event) {
    console.log("Connected to WebSocket");
};

ws.onmessage = function(event) {
    const messages = document.getElementById("messages");
    const message = document.createElement("p");
    message.textContent = "Message from server: " + event.data;
    messages.appendChild(message);
};

ws.onclose = function(event) {
    console.log("Disconnected from WebSocket");
};

ws.onerror = function(event) {
    console.error("WebSocket error:", event);
};
