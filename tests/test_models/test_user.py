#!/usr/bin/python3
"""Unitesst for User class"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Set up for the tests.
        Creates instances for two users.
        """
        self.my_user = User()
        self.my_user.first_name = "Betty"
        self.my_user.last_name = "Bar"
        self.my_user.email = "airbnb@mail.com"
        self.my_user.password = "root"
        self.my_user.save()

        self.my_user2 = User()
        self.my_user2.first_name = "John"
        self.my_user2.email = "airbnb2@mail.com"
        self.my_user2.password = "root"
        self.my_user2.save()

        self.my_user3 = User()

    def test_id(self):
        """Test id """
        self.assertNotEqual(self.my_user.id, self.my_user2.id)

    def test_attributes(self):
        """Test the attributes of User"""
        self.assertTrue(hasattr(self.my_user, "email"))
        self.assertTrue(hasattr(self.my_user, "password"))
        self.assertTrue(hasattr(self.my_user, "first_name"))
        self.assertTrue(hasattr(self.my_user, "last_name"))

    def test_attributes_default(self):
        """ Test attributes default for User """
        self.assertEqual(self.my_user3.email, "")
        self.assertEqual(self.my_user3.password, "")
        self.assertEqual(self.my_user3.first_name, "")
        self.assertEqual(self.my_user3.last_name, "")

    def test_inheritance(self):
        """Test if User inherits from BaseModel"""
        self.assertTrue(issubclass(type(self.my_user), BaseModel))

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.my_user), "[User] ({}) {}".
                         format(self.my_user.id, self.my_user.__dict__))

    def test_to_dict(self):
        """Test the to_dict method"""
        my_user_dict = self.my_user.to_dict()
        self.assertEqual(type(my_user_dict), dict)
        self.assertTrue("to_dict" in dir(self.my_user))

    def test_save(self):
        """Test the save method"""
        self.my_user.save()
        self.assertNotEqual(self.my_user.created_at, self.my_user.updated_at)

    def test_create_user(self):
        """Test the create method"""
        self.my_user2.save()
        self.assertNotEqual(self.my_user2.created_at, self.my_user2.updated_at)


if __name__ == '__main__':
    unittest.main()
