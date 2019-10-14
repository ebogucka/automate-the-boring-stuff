#!/usr/bin/env python3

import unittest
from strip import strip


class TestStrip(unittest.TestCase):
    def test_whitespace(self):
        text = "Cats are good pets, for they are clean and are not noisy."
        self.assertEqual(strip(f"     \t       {text}    \n"), text)

    def test_characters(self):
        text = "Cats are good pets, for they are clean and are not noisy."
        self.assertEqual(strip(f"abccaa{text}cbaaa", "abc"), text)

    def test_characters_not_present(self):
        text = "Cats are good pets, for they are clean and are not noisy."
        self.assertEqual(strip(text, "xyz"), text)

    def test_empty(self):
        self.assertEqual(strip("     \t          \n"), "")


if __name__ == "__main__":
    unittest.main()
