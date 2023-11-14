#!/usr/bin/python3
"""Unitesst for Review class"""""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.my_review = Review()
        self.my_review.place_id = "place1"
        self.my_review.user_id = "user1"
        self.my_review.text = "Great place!"

        self.review2 = Review()

    def test_id(self):
        """Test id """
        self.assertNotEqual(self.my_review.id, self.review2.id)

    def test_attributes(self):
        """Test the attributes of Review"""
        self.assertEqual(self.my_review.place_id, "place1")
        self.assertEqual(self.my_review.user_id, "user1")
        self.assertEqual(self.my_review.text, "Great place!")

    def test_attributes_default(self):
        """ Test attributes default for Review """
        self.assertEqual(self.review2.place_id, "")
        self.assertEqual(self.review2.user_id, "")
        self.assertEqual(self.review2.text, "")

    def test_inheritance(self):
        """Test if Review inherits from BaseModel"""
        self.assertTrue(issubclass(type(self.my_review), BaseModel))

    def to_dict(self):
        """Test to_dict method"""
        self.assertEqual('to_dict' in dir(self.my_review), True)

    def test_str(self):
        """Test __str__ method"""
        self.assertEqual(str(self.my_review),
                         "[Review] ({}) {}".format(self.my_review.id,
                                                   self.my_review.__dict__))

    def test_save(self):
        """Test save method"""
        self.my_review.save()
        self.assertNotEqual(self.my_review.created_at,
                            self.my_review.updated_at)


if __name__ == '__main__':
    unittest.main()
