# orders
A demo order system


## API

REST API Endpoints for Orders:
GET    /orders           # List all orders
POST   /orders           # Create new order
GET    /orders/{id}      # Get specific order (UUID or readable ID)
PUT    /orders/{id}      # Update order (full replacement)
DELETE /orders/{id}      # Delete order
GET    /health           # Health check
Operations:

List - Return all orders as JSON array
Create - Accept order data, return new order with UUID + readable ID
Read - Find order by UUID or readable ID, return order data
Update - Replace order data with new information
Delete - Remove order, return 204 No Content
Health - Service status check

Order ID Format:

UUID: 550e8400-e29b-41d4-a716-446655440000 (primary, for system use)
Readable ID: ORD-001, ORD-002 (for customer invoices, support tickets)

HTTP Status Codes:

200 OK (GET operations)
201 Created (POST)
204 No Content (DELETE)
400 Bad Request (validation errors)
404 Not Found (order doesn't exist)
500 Internal Server Error (file lock/storage issues)