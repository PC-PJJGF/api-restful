import unittest
from main import main

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.client = main.test_client()

    def test_get_tareas(self):
        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)
