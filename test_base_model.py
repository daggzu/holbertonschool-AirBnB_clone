#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
"""
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel



class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""
    def test_init(self):
        bm = BaseModel()
        self.assertTrue(isinstance(bm, BaseModel))
        self.assertTrue(hasattr(bm, 'id'))
        self.assertTrue(hasattr(bm, 'created_at'))
        self.assertTrue(hasattr(bm, 'updated_at'))
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_str(self):
        bm = BaseModel()
        expected_str = f"[BaseModel] ({bm.id}) {bm.__dict__}"
        self.assertEqual(str(bm), expected_str)

    def test_save(self):
        bm = BaseModel()
        initial_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(bm.updated_at, initial_updated_at)

    def test_to_dict(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertEqual(bm_dict['created_at'], bm.created_at.isoformat())
        self.assertEqual(bm_dict['updated_at'], bm.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
