#!/usr/bin/python3
"""File storage class module"""

from models.base_model import BaseModel
import os.path
import json


class FileStorage():
    """
    Actions carried out by the FileStorage Class
    within generated objects and JSON files
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """method returns the __objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        if obj:
            key = type(obj).__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        d = {}
        for key, obj in FileStorage.__objects.items():
            d[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_f:
            json.dump(d, json_f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path)
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as js_f:
                for key, obj in json.loads(js_f.read()).items():
                    obj = eval(obj['__class__'])(**obj)
                    FileStorage.__objects[key] = obj
