# test_orders.py
import unittest
import json
import uuid
from orders_server import app, all_orders  # Replace 'your_flask_app' with your actual file name


class TestOrdersAPI(unittest.TestCase):
    """Unit tests for the Orders Flask API"""
    
    def setUp(self):
        """Set up test fixtures before each test method"""
        app.config['TESTING'] = True
        self.client = app.test_client()  # Then get client


        # Clear all_orders dictionary before each test
        all_orders.clear()
        
        # Sample order data for testing
        self.sample_order = {
            'prod': 'laptop',
            'quantity': 2
        }
    
    def test_new_order(self):
        """Test POST /orders creates a new order and returns an ID"""
        # Send POST request to create new order
        response = self.client.post('/orders',
                               data=json.dumps(self.sample_order),
                               content_type='application/json')
        
        # Check response status
        self.assertEqual(response.status_code, 200)
        
        # Parse response data
        response_data = json.loads(response.data)
        
        # Test that response contains an ID
        self.assertIn('id', response_data)
        returned_id = response_data['id']
        
        # Test that returned ID is a valid UUID format
        uuid_obj = uuid.UUID(returned_id)  # This will raise ValueError if invalid
        self.assertIsInstance(uuid_obj, uuid.UUID)
        
        
    
    def test_get_all_orders(self):
        """Test GET /orders returns all stored orders"""
        # First, create a couple of orders using POST
        order1 = {'prod': 'mouse', 'quantity': 1}
        order2 = {'prod': 'keyboard', 'quantity': 1}
        
        # Post first order
        response1 = self.client.post('/orders',
                                data=json.dumps(order1),
                                content_type='application/json')
        id1 = json.loads(response1.data)['id']
        
        # Post second order
        response2 = self.client.post('/orders',
                                data=json.dumps(order2),
                                content_type='application/json')
        id2 = json.loads(response2.data)['id']
        
        # Now test GET /orders
        response = self.client.get('/orders')
        self.assertEqual(response.status_code, 200)
        
        # Parse response data
        orders_data = json.loads(response.data)
        
        # Test that both orders are in the response
        self.assertIn(id1, orders_data)
        self.assertIn(id2, orders_data)
        self.assertIn('itzik', orders_data)  # Your code adds this key
        
        # Test that the orders contain correct data
        self.assertEqual(orders_data[id1]['prod'], 'mouse')
        self.assertEqual(orders_data[id1]['quantity'], 1)
        self.assertEqual(orders_data[id2]['prod'], 'keyboard')
        self.assertEqual(orders_data[id2]['quantity'], 1)
    
    def tearDown(self):
        """Clean up after each test"""
        # Clear the orders dictionary
        all_orders.clear()


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)