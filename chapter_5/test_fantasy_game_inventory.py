#!/usr/bin/env python3

import unittest
from fantasy_game_inventory import add_to_inventory


class TestAddToInventory(unittest.TestCase):
    def test_list(self):
        """Test that it can add items from a list"""
        inventory = {"gold coin": 42, "rope": 1}
        new_items = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
        expected_inventory = {"gold coin": 45, "rope": 1, "dagger": 1, "ruby": 1}
        result = add_to_inventory(inventory, new_items)
        self.assertEqual(result, expected_inventory)

    def test_list_empty(self):
        """Test adding an empty list"""
        inventory = {"gold coin": 42, "rope": 1}
        result = add_to_inventory(inventory, [])
        self.assertEqual(result, inventory)


if __name__ == "__main__":
    unittest.main()
