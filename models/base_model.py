#!/usr/bin/python3
"""BaseModel Module"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """BaseModels class"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        # Ensuring "id," "created_at," and "updated_at" are explicitly initialized.
        self.id = kwargs.get("id", self.id)
        self.created_at = kwargs.get("created_at", self.created_at)
        self.updated_at = kwargs.get("updated_at", self.updated_at)

        # Notify the storage system of the new instance.
        models.storage.new(self)

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
        if isinstance(self.created_at, datetime):
            dictionary["created_at"] = self.created_at.isoformat()
        if isinstance(self.updated_at, datetime):
            dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
