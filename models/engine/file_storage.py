import json
from models.base_model import BaseModel
from json import dump, load


class FileStorage:
    """This class handles the serialization and deserialization of objects to and from a JSON file."""

    # Private Attributes
    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store objects by <class name>.id

    # Methods
    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        objects = FileStorage.__objects
        dict_from_obj = {key: obj.to_dict() for key, obj in objects.items()}

        with open(FileStorage.__file_path, 'w') as file:
            dump(dict_from_obj, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path) as file:
                dict_from_json = load(file)
                for obj in dict_from_json.values():
                    self.new(eval(obj['__class__'])(**obj))
        except Exception:
            return
