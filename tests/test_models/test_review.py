#!/usr/bin/python3
"""
Tests for the Review Model
"""


import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_review_initialization(self):
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_attributes(self):
        review = Review()
        # Set attributes and check if they are properly set

    def test_review_methods(self):
        review = Review()
        # Call methods and assert the expected outcomes

if __name__ == '__main__':
    unittest.main()
