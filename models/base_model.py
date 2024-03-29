#!/usr/bin/python3
""" This file contains the base model BaseModel"""


import uuid
from datetime import datetime
from  models import storage


class BaseModel():
    """ Class BaseModel"""
    def __init__(self, *args, **kwargs):
        """ Constructor to basemodel class"""
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "update_at":
                    val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
                    continue
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        return string representation of BaseModel class
        """
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Update the update_at attribute """
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dictionary representation of BaseModel class
        """
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = type(self).__name__
        base_dict["created_at"] = base_dict["created_at"].isoformat()
        base_dict["updated_at"] = base_dict["updated_at"].isoformat()

        return base_dict
