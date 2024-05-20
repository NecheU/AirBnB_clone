#!/usr/bin/python3
import uuid
from datetime import datetime
import models

"""
Module for the basemodel


classes:
    BaseModel: Parent class of the project
"""


class BaseModel:
    """
    Base model class
    methods:
    __init__(self, *args, **kwargs)
    __str__(self)
    __save(self)
    to_dict(self)
    """
    def __init__(self, *args, **kwargs):
        """Initialization of the Base Model class

        Args:
        *args: anonymous arguments
        **kwargs: Keyword arguments

        Attributes:
        id (str) : uuid4 assigned to the class
        created_at (dateteime) : Current date and time of instance
        updated_at (dateteime) : Current date and time of instance

        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of the class"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Saves progress of the updated_at attributte"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
