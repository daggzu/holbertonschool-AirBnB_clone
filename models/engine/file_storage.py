#!/usr/bin/python3
"""This module defines the FileStorage class"""

import json
from models.base_model import BaseModel
from models.user import User  # Import the User class
from json import dump, load


class FileStorage:
    """This class handles the serialization and deserialization of objects to and from a JSON file."""

    # Private Attributes
    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store objects by <class name>.id

    def __init__(self):
        """Initialize FileStorage and add User class to classes dictionary."""
        self.__class_dict = {
            "BaseModel": BaseModel,
            "User": User  # Add User to the classes dictionary
            # Add more classes here as needed
        }

    # Methods
    def all(self, cls=None):
        """Returns the dictionary __objects filtered by class name."""
        if cls is None:
            return FileStorage.__objects
        else:
            class_name = cls.__name__
            filtered_objects = {
                key: obj for key, obj in FileStorage.__objects.items() if class_name in key
            }
            return filtered_objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.____name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                dict_from_json = load(file)
                for key, value in dict_from_json.items():
                    class_name = value["__class__"]
                    obj = self.__class_dict[class_name](**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
