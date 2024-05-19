#!/usr/bin/python3

""" Module for the State class
    and its method
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Responsible for the state features.

    Attributes:
        name (str): Name of state
    """
    name = ""
