#!/usr/bin/python3
# & This module defines the class User

# & Import the BaseModel class from the models.base_model module
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    # & Define the attributes of the User class
    email = ""  # & The email of the user, initialized as an empty string
    password = ""  # & The password of the user, initialized as an empty string
    first_name = ""  # & The first name of the user, init as an empty string
    last_name = ""  # & The last name of the user, init as an empty string

    def __str__(self):
        """Returns the string representation of the User instance"""
        # & Format: [<class name>] (<self.id>) <self.__dict__>
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
