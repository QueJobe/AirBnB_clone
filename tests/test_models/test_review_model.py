#!/usr/bin/python3

"""
    Tests cases for review class
"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
        test case revire class
    """

    def test_Review_inheritance(self):
        """
            Verifies if the Review class is derived from BaseModel
        """
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)

    def test_Review_attributes(self):
        """
            Verify that the place_id, user_id, and text
            properties are present in the Review class
        """
        new_review = Review()
        self.assertTrue("place_id" in new_review.__dir__())
        self.assertTrue("user_id" in new_review.__dir__())
        self.assertTrue("text" in new_review.__dir__())

    def test_Review_attributes(self):
        """
            Verify that the Review class has the
            place_id, user_id, and text properties
        """
        new_review = Review()
        place_id = getattr(new_review, "place_id")
        user_id = getattr(new_review, "user_id")
        text = getattr(new_review, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)
