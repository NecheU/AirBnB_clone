#!/usr/bin/python3
"""User class for the project
"""


from models.base_model import BaseModel
import json

class User(BaseModel):
    """
    Class that inherits from the BaseModel Parent Class

    Attributes:
    email: Email address
    password: Password
    first_name: First Name
    last_name: Last Name

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
