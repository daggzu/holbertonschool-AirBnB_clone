#!/usr/bin/python3
import json

class FileStorage:
    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store all objects

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.____name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects if the file exists."""
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    class_name, obj_id = key.split(".")
                    class_name = class_name.replace("_", " ")
                    obj_class = models.class_from_name(class_name)
                    new_obj = obj_class(**obj_data)
                    FileStorage.__objects[key] = new_obj
        except FileNotFoundError:
            pass

