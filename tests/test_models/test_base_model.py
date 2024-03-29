#!/usr/bin/python3
"""Basic template file unit test: class and methods"""

import unittest
import os
from models import base_model
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class Test_Base_Model_outputs(unittest.TestCase):
    """BaseModel class unittest and test cases"""

    def test_unique_id(self):
        """
        test_unique_id to tests if an ID is unique.
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1, instance2)

    def test_id_type(self):
        """
        the test_id_type function, which verifies that the id type is proper
        """
        instance1 = BaseModel()
        self.assertEqual('<class \'str\'>', str(type(instance1.id)))

    def test_exec_file(self):
        """
        Use the test_exec_file function to determine whether a file has
        permissions to read, write, and execute,permissions
        """
        read = os.access('models/base_model.py', os.R_OK)
        self.assertEqual(True, read)
        write = os.access('models/base_model.py', os.W_OK)
        self.assertEqual(True, write)
        exec = os.access('models/base_model.py', os.X_OK)
        self.assertEqual(True, exec)

    def test_save(self):
        """
        Use the test_save function to see if the update_at attribute
        is updated each time the instance is saved.
        """
        instance1 = BaseModel()
        attr_updated_before_save = instance1.updated_at
        instance1.save()
        attr_updated_after_save = instance1.updated_at
        self.assertNotEqual(attr_updated_before_save, attr_updated_after_save)

    def test_to_dict(self):
        """
        The test_to_dict function checks to see if a dictionary is
        returned and whether the updated_at and created_at
        properties are formatted correctly.
        """
        instance1 = BaseModel()
        instance1_User = User()
        # test type of return
        self.assertEqual('<class \'dict\'>', str(type(instance1.to_dict())))

        updated_expected_format = instance1.updated_at.isoformat()
        created_expected_format = instance1.created_at.isoformat()
        class_attr_value_expected = type(instance1_User).__name__
        updated_actual_format = instance1.to_dict()["updated_at"]
        created_actual_format = instance1.to_dict()["created_at"]
        class_attr_value_get = instance1_User.to_dict()['__class__']
        # test format inside the dictionary
        self.assertEqual(updated_expected_format, updated_actual_format)
        self.assertEqual(created_expected_format, created_actual_format)
        self.assertEqual(class_attr_value_expected, class_attr_value_get)

