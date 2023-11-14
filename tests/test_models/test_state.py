#!/usr/bin/python3
"""Unitesst for State class"""""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.my_state = State()
        self.my_state.name = "California"

        self.my_state2 = State()
        self.my_state2.name = "Alabama"

        self.state3 = State()

    def test_id(self):
        """Test id """
        self.assertNotEqual(self.my_state.id, self.my_state2.id)

    def test_attributes(self):
        """Test the attributes of State"""
        self.assertEqual(self.my_state.name, "California")
        self.assertEqual(self.my_state2.name, "Alabama")

    def test_attributes_default(self):
        """ Test attributes default for State """
        self.assertEqual(self.state3.name, "")

    def test_inheritance(self):
        """Test if State inherits from BaseModel"""
        self.assertTrue(issubclass(type(self.my_state), BaseModel))

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.my_state), "[State] ({}) {}".
                         format(self.my_state.id, self.my_state.__dict__))

    def test_to_dict(self):
        """Test the to_dict method"""
        self.assertEqual('to_dict' in dir(self.my_state), True)

    def test_save(self):
        """Test save method"""
        self.my_state.save()
        self.assertNotEqual(self.my_state.created_at,
                            self.my_state.updated_at)


if __name__ == '__main__':
    unittest.main()
