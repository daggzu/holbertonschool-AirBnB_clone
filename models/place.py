#!/usr/bin/python3
# & This module defines the class Place

# & Import the BaseModel class from the models.base_model module
from models.base_model import BaseModel


class Place(BaseModel):
    """This class defines a place by various attributes"""
    # & Define the attributes of the Place class
    city_id = ""  # & The ID of the city the place  init as an empty string
    user_id = ""  # & The ID of the user  init as an empty string
    name = ""  # & The name of the place, initialized as an empty string
    description = ""  # & The description of the place, init as an empty string
    number_rooms = 0  # & The number of rooms in the place, initialized as 0
    number_bathrooms = 0  # & The number of bathrooms in the place, init as 0
    max_guest = 0  # & The maximum number of guests  init as 0
    price_by_night = 0  # & The price per night to stay at the place, init as 0
    latitude = 0.0  # & The latitude of the place's location, init as 0.0
    longitude = 0.0  # & The longitude of the place's location, init as 0.0
    # & A list of IDs of the amenities the place offers, init as an empty list
    amenity_ids = []

    def __str__(self):
        """Returns the string representation of the User instance"""
        # & Format: [<class name>] (<self.id>) <self.__dict__>
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
