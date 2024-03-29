#!/usr/bin/python3
"""
File storage test module
"""

import os
import json
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """ Ensure file.json does not exist before each test """
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.storage = FileStorage()

    def tearDown(self):
        """ Remove file.json after each test """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_empty(self):
        """ Test if all method returns an empty dictionary when no objects are stored"""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """ Test if new method adds an object to the __objects dictionary"""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn("BaseModel." + obj.id, self.storage.all())

    def test_save_reload(self):
        """ Test if save and reload methods correctly save and load objects"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        self.assertIn("BaseModel." + obj.id, self.storage.all())

if __name__ == '__main__':
    unittest.main()

