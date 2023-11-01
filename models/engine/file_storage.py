# models/engine/file_storage.py

import json

class FileStorage:
    """This class handles the serialization and deserialization of objects to and from a JSON file."""
    
    # Private Attributes
    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store objects by <class name>.id

    # Methods
    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        temp_dict = {}
        for key, obj in self.__objects.items():
            temp_dict[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(temp_dict, file)

def reload(self):
    """Deserializes the JSON file to __objects"""
    # Try to open the file and load the JSON
    try:
        with open(self.__file_path, "r") as f:
            self.__objects = json.loads(f.read())
            # Convert dictionaries back to objects
            for key, obj in self.__objects.items():
                self.__objects[key] = eval(obj["__class__"])(**obj)
    # If the file doesn't exist, do nothing
    except FileNotFoundError:
        pass
