import unittest
from app.main import welcome

class TestWelcome(unittest.TestCase):

    def test_welcome_message(self):
        self.assertEqual(
            welcome(),
            "Welcome to my first GCP DevOps application!"
        )

if __name__ == "__main__":
    unittest.main()
