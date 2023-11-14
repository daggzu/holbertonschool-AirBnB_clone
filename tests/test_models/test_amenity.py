#!/usr/bin/python3
"""Unitesst for Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.my_amenity = Amenity()
        self.my_amenity.name = "Pool"
        # & Empty object
        self.amenity2 = Amenity()

    def tearDown(self):
        """Tear down for tests"""
        del self.my_amenity
        del self.amenity2

    def test_attributes(self):
        """Test the attributes of Amenity"""
        self.assertEqual(self.my_amenity.name, "Pool")

    def test_attributes_default(self):
        """ Test attributes default for Amenity """
        self.assertEqual(self.amenity2.name, "")

    def test_save(self):
        """Check for updated_at after save()"""
        self.my_amenity.save()
        self.assertNotEqual(self.my_amenity.created_at,
                            self.my_amenity.updated_at)

    def test_str(self):
        """Test __str__ method"""
        self.assertEqual(str(self.my_amenity),
                         "[Amenity] ({}) {}".format(self.my_amenity.id,
                                                    self.my_amenity.__dict__))

    def test_to_dict(self):
        """Test to_dict method"""
        self.assertEqual('to_dict' in dir(self.my_amenity), True)

    def test_id(self):
        """Test id """
        self.assertNotEqual(self.my_amenity.id, self.amenity2.id)


if __name__ == '__main__':
    unittest.main()
