# tests/test_model1.py

import unittest
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import from src
from src.model import MetroCard

class TestMetroCard(unittest.TestCase):
    def test_add_balance(self):
        card = MetroCard("MC100", 100)
        card.add_balance(50)
        self.assertEqual(card.balance, 150)

    def test_update_src(self):
        card = MetroCard("MC101", 200)
        card.update_src("CENTRAL")
        self.assertEqual(card.src, "CENTRAL")

if __name__ == '__main__':
    unittest.main()
