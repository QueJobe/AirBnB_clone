#!/usr/bin/python3
"""
    This file contains the BaseModel class module
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
        BaseModel class.
    """
    def __init__(self, *args, **kwargs):
        """
            Constructor for basemodel class
        """
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """
            Return the BaseModel class's string representation.
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        """
            Return string representation of BaseModel class
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
            Add new to the updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            Provide the BaseModel class's dictionary representation back.
        """
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        cp_dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cp_dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return (cp_dct)
