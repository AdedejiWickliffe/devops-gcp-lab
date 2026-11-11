import unittest
from app.main import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json["message"],
            "Welcome to my first GCP DevOps web application!"
        )

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "healthy")

if __name__ == "__main__":
    unittest.main()
