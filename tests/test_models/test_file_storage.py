import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.save()
        self.model_id = self.model.id

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIn("BaseModel.{}".format(self.model_id), all_objects)

    def test_new(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        all_objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(new_model.id), all_objects)

    def test_save(self):
        all_objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(self.model_id), all_objects)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        all_objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(self.model_id), all_objects)
        self.storage.save()
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(self.model_id), all_objects)

if __name__ == '__main__':
    unittest.main()
