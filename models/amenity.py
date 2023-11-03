#!/usr/bin/python3
# & This module defines the class Amenity

# & Import the BaseModel class from the models.base_model module
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class defines an amenity by various attributes"""
    # & Define the attributes of the Amenity class
    name = ""  # & The name of the amenity, initialized as an empty string
