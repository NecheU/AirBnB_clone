#!/usr/bin/python3
"""Storage class Module
"""


import os
import json
from models import base_model, user, state, city, amenity, place, review


class FileStorage:
    """File Storage class for the project

    file_path: file path of json file
    objects: Ibjects of the project
    """

    __file_path = "file.json"
    __objects = {}

    class_dict = {"BaseModel": "base_model", "User": "user",
                  "City": "city", "State": "state",
                  "Amenity": "amenity", "Place": "place",
                  "Review": "review"}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes the dict into a json file"""
        obj = {key: val.to_dict() for key, val in self.__objects.items()}
        with open(self.__file_path, "w") as json_file:
            json.dump(obj, json_file)

    def reload(self):
        """Deserialises the json file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                json_dict = json.load(f)
                for obj in json_dict.values():
                    class_name = obj['__class__']
                    module_name = self.class_dict[class_name]
                    del obj['__class__']
                    self.new(eval(f'{module_name}.{class_name}')(**obj))

    def classes(self):
        """returns a class"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes
