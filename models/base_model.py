#!/usr/bin/python3
""" This file contains the base model BaseModel"""


import uuid
from datetime import datetime


class BaseModel():
    """ Class BaseModel"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        return string representation of BaseModel class
        """
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Update the update_at attribute """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        Return dictionary representation of BaseModel class
        """
        base_dict = self.__dict__.copy()
        base_dict['__class__'] = self.__class__.__name__
        base_dict['created_at'] = self.created_at.isoformat()
        base_dict['updated_at'] = self.updated_at.isoformat()

        return base_dict
