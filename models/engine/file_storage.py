#!/usr/bin/python3
"""
    This file contains file storage class
"""
import json
import models


class FileStorage:
    """
        this class Deserializes and serializes instances to a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Returns dictionary objects
        """
        return self.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
            __objects attribute is serialized to a JSON file.
        """
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """
            The JSON file is deserialized to __objects.
        """
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass
