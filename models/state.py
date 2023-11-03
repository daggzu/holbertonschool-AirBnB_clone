#!/usr/bin/python3
"""This module defines the class State

    Import the BaseModel class from the models.base_model module
from models.base_model import BaseModel
"""


class State(BaseModel):
    """This class defines a state by various attributes"""
    # & Define the attributes of the State class
    name = ""  # & The name of the state, initialized as an empty string

    def __str__(self):
        """Returns the string representation of the User instance"""
        # & Format: [<class name>] (<self.id>) <self.__dict__>
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
