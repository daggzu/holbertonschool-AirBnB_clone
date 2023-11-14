#!/usr/bin/python3
"""This module defines the FileStorage class"""
# & Import necessary modules
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances"""
    # & Private Attributes
    __file_path = "file.json"  # & Path to the JSON file
    __objects = {}  # & Empty dictionary to store objects

    # & Methods

    def all(self):
        """Returns the dictionary __objects
        that contains all objects"""
        # & Return all objects
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        # & Create a key with object's class name and id
        key = obj.__class__.__name__ + "." + str(obj.id)
        # & Add the object to the dictionary
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        # & Create a temporary dictionary to store objects
        temp_dict = {}

        # & Open the file and dump the objects as JSON
        with open(self.__file_path, "w") as f:
            for key, obj in self.__objects.items():
                # & update updated_at
                obj.updated_at = datetime.now()
                temp_dict[key] = obj.to_dict()
            json.dump(temp_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        # & Try to open the file and load the JSON
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.loads(f.read())
                # & Convert dictionaries back to objects
                for key, obj in self.__objects.items():
                    self.__objects[key] = eval(obj["__class__"])(**obj)
        # & If the file doesn't exist, do nothing
        except FileNotFoundError:
            pass
