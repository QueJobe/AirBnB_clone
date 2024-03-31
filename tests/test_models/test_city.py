#!/usr/bin/python3

"""
    City class test cases
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestUser(unittest.TestCase):
    """
        test cases for city class
    """

    def test_City_inheritance(self):
        """
            verifying if the City class is inherited from BaseModel
        """
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_User_attributes(self):
        new_city = City()
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())

    def test_type_name(self):
        """
            name type test
        """
        new_city = City()
        name = getattr(new_city, "name")
        self.assertIsInstance(name, str)

    def test_type_name(self):
        """
            Verify the name type
        """
        new_city = City()
        name = getattr(new_city, "state_id")
        self.assertIsInstance(name, str)
