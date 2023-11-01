#!/usr/bin/python3
"""BaseModel Module"""
import uuid
from datetime import datetime
import models  

class BaseModel:
    """BaseModels class"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel."""
        #Check if keyword arguments (kwargs) were provided.
        if kwargs:
            for key, value in kwargs.items():
                """Skip the '__class__' attribute if present, as it's not used for initialization."""
                if key == "__class__":
                    pass
                """Parse and set 'created_at' and 'updated_at' attributes as datetime objects."""
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                """Set other attributes from kwargs."""
                else:
                    setattr(self, key, value)
        else:
            """If no kwargs are provided, initialize default values for 'id', 'created_at', and 'updated_at'."""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at with current time and save to storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert to dictionary"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
