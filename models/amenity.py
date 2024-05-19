#!/usr/bin/python3

""" Module for the amenity class
    and its method
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Responsible for the amenity features.

    Attributes:
        name (str): Name of amenity
    """
    name = ""
