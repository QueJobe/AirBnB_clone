#!/usr/bin/python3
"""City class module file"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    class city that inherits from Basemodel
    """
    state_id = ""
    name = ""
