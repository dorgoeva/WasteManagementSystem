import unittest
from src.models import WasteRequest

class TestWasteRequest(unittest.TestCase):
    def test_request_init(self):
        req = WasteRequest(1, "Aliya", "Plastic", "2025-04-10")
        self.assertEqual(req.user_name, "Aliya")

if __name__ == "__main__":
    unittest.main()
