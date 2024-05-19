#!/usr/bin/python3

""" Module for the Review class
    and its method
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Responsible for the review class features.

    Attributes:
        place_id (str): Place Id of review
        user_id (str): User ID of review
        text (str): Review text
    """
    place_id = ""
    user_id = ""
    text = ""
