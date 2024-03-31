#!/usr/bin/python3
"""
    Test cases forstate class
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
        State class tests
    """

    def test_State_inheritence(self):
        """
            Check if the State class is descended from the BaseModel.
        """
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_State_attributes(self):
        """
            Verify if the attribute {name} is present in the State class.
        """
        new_state = State()
        self.assertTrue("name" in new_state.__dir__())

    def test_State_attributes_type(self):
        """
            Verify that the name of the State class
            attribute is class type str.
        """
        new_state = State()
        name = getattr(new_state, "name")
        self.assertIsInstance(name, str)
