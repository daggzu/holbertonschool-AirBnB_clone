#!/usr/bin/python3
"""Unitesst for City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.my_city = City()
        self.my_city.state_id = "CA"
        self.my_city.name = "San Francisco"
        # & Empty object
        self.city2 = City()

    def tearDown(self):
        """Tear down for tests"""
        del self.my_city
        del self.city2

    def test_attributes(self):
        """Test the attributes of City"""
        self.assertEqual(self.my_city.state_id, "CA")
        self.assertEqual(self.my_city.name, "San Francisco")

    def test_attributes_default(self):
        """ Test attributes default for City """
        self.assertEqual(self.city2.state_id, "")
        self.assertEqual(self.city2.name, "")

    def test_save(self):
        """Check for updated_at after save()"""
        self.my_city.save()
        self.assertNotEqual(self.my_city.created_at,
                            self.my_city.updated_at)

    def test_str(self):
        """Test __str__ method"""
        self.assertEqual(str(self.my_city),
                         "[City] ({}) {}".format(self.my_city.id,
                                                 self.my_city.__dict__))

    def test_to_dict(self):
        """Test to_dict method"""
        self.assertEqual('to_dict' in dir(self.my_city), True)

    def test_id(self):
        """Test id """
        self.assertNotEqual(self.my_city.id, self.city2.id)


if __name__ == '__main__':
    unittest.main()
