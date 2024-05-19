#!/usr/bin/python3

""" Module for the City class
    and its method
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Responsible for the state features.

    Attributes:
        state_id (str) : State Id i.e State.id
        name (str): Name of state
    """
    state_id = ""
    name = ""
