#!/usr/bin/python3
"""This module contains the review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    class review inherits from BaseModel class
    """
    place_id = ""
    user_id = ""
    text = ""
