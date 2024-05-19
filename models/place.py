#!/usr/bin/python3

""" Module for the Place class
    and its method
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Responsible for the state features.

    Attributes:
        city_id (str): It would be the City.id
        user_id (str): User Id
        name (str): Name of place
        description (str): Description
        number_rooms (int): Number of rooms
        number_bathrooms (int): Number of bathrooms
        max_guest (int): Maximum guest
        price_by_night (int): Price per night
        latitude (float): Latitude of city
        longitude (float): Longitude of place
        amenity_ids (list of string): Ids of amenities
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
