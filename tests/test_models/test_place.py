#!/usr/bin/python3
"""Unitesst for Place class"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.my_place = Place()
        self.my_place.city_id = "SF"
        self.my_place.user_id = "user1"
        self.my_place.name = "My Place"
        self.my_place.description = "A nice place"
        self.my_place.number_rooms = 3
        self.my_place.number_bathrooms = 2
        self.my_place.max_guest = 4
        self.my_place.price_by_night = 100
        self.my_place.latitude = 37.7749
        self.my_place.longitude = -122.4194
        self.my_place.amenity_ids = ["amenity1", "amenity2"]
        # & Empty object
        self.place2 = Place()

    def test_attributes(self):
        """Test the attributes of Place"""
        self.assertEqual(self.my_place.city_id, "SF")
        self.assertEqual(self.my_place.user_id, "user1")
        self.assertEqual(self.my_place.name, "My Place")
        self.assertEqual(self.my_place.description, "A nice place")
        self.assertEqual(self.my_place.number_rooms, 3)
        self.assertEqual(self.my_place.number_bathrooms, 2)
        self.assertEqual(self.my_place.max_guest, 4)
        self.assertEqual(self.my_place.price_by_night, 100)
        self.assertEqual(self.my_place.latitude, 37.7749)
        self.assertEqual(self.my_place.longitude, -122.4194)
        self.assertEqual(self.my_place.amenity_ids, ["amenity1", "amenity2"])

    def test_attributes_default(self):
        """ Test attributes default for Place """
        self.assertEqual(self.place2.city_id, "")
        self.assertEqual(self.place2.user_id, "")
        self.assertEqual(self.place2.name, "")
        self.assertEqual(self.place2.description, "")
        self.assertEqual(self.place2.number_rooms, 0)
        self.assertEqual(self.place2.number_bathrooms, 0)
        self.assertEqual(self.place2.max_guest, 0)
        self.assertEqual(self.place2.price_by_night, 0)
        self.assertEqual(self.place2.latitude, 0.0)
        self.assertEqual(self.place2.longitude, 0.0)
        self.assertEqual(self.place2.amenity_ids, [])

    def test_save(self):
        """Check for updated_at after save()"""
        self.my_place.save()
        self.assertNotEqual(self.my_place.created_at,
                            self.my_place.updated_at)

    def test_str(self):
        """Test __str__ method"""
        self.assertEqual(str(self.my_place),
                         "[Place] ({}) {}".format(self.my_place.id,
                                                  self.my_place.__dict__))

    def test_to_dict(self):
        """Test to_dict method"""
        self.assertEqual('to_dict' in dir(self.my_place), True)

    def test_inheritance(self):
        """Test if Place inherits from BaseModel"""
        self.assertTrue(issubclass(type(self.my_place), BaseModel))

    def test_method(self):
        """Test the methods"""
        self.assertTrue(hasattr(self.my_place, "to_dict"))
        self.assertTrue(hasattr(self.my_place, "save"))


if __name__ == '__main__':
    unittest.main()
