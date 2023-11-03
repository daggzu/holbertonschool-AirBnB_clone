#!/usr/bin/python3
# & This module defines the class City

# & Import the BaseModel class from the models.base_model module
from models.base_model import BaseModel


class City(BaseModel):
    """This class defines a city by various attributes"""
    # & Define the attributes of the City class
    state_id = ""  # & The ID of the state the city initialized as an empty str
    name = ""  # & The name of the city, initialized as an empty string

    def __str__(self):
        """Returns the string representation of the User instance"""
        # & Format: [<class name>] (<self.id>) <self.__dict__>
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
