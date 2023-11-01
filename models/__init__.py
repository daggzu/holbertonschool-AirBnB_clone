#!/usr/bin/python3
"""This module creates a unique FileStorage instance for the application
"""
from models.engine.file_storage import FileStorage
# & FileStorage instance
storage = FileStorage()
# & Reload objects
storage.reload()
