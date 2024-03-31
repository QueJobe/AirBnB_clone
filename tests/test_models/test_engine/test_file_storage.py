#!/usr/bin/python3
"""
    file_storage module test file
"""

import os
import time
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class testFileStorage(unittest.TestCase):
    """
        FileStorage class testing
    """

    def setUp(self):
        """
            Test cases set up
        """
        self.storage = FileStorage()
        self.my_model = BaseModel()

    def tearDown(self):
        """
            Deleting files
        """

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_return_type(self):
        """
            checks the data type of the all method's return value.
        """
        storage_all = self.storage.all()
        self.assertIsInstance(storage_all, dict)

    def test_new_method(self):
        """
            Verifies that the new approach sets the appropriate
            key-value pair in the FileStorage.__object attribute.
        """
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_objects_value_type(self):
        """
            Verifies if the value stored in FileStorage.__object
            is of the type obj.__class__.__name__.
        """
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        val = self.storage._FileStorage__objects[key]
        self.assertIsInstance(self.my_model, type(val))

    def test_save_file_exists(self):
        """
            Verifies the creation of a file with the name file.JSON
        """
        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_file_read(self):
        """
            Verifying the files' contents within the file.JSON
        """
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as fd:
            content = json.load(fd)

        self.assertTrue(type(content) is dict)

    def test_the_type_file_content(self):
        """
            examining the kind of information included in the file.
        """
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as fd:
            content = fd.read()

        self.assertIsInstance(content, str)

    def test_reaload_without_file(self):
        """
            Verifies that nothing occurs upon file.JSON
            is not present, and reload is initiated.
        """

        try:
            self.storage.reload()
            self.assertTrue(True)
        except:
            self.assertTrue(False)
