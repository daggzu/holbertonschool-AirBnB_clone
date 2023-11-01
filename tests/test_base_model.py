#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
"""
import unittest
import models
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""
