#!/usr/bin/python3
"""
testing basemodel
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        my_model = BaseModel()

        initial_updated = my_model.updated_at
        current_updated = my_model.save()
        self.assertNotEqual(initial_updated, current_updated)

    def test_to_dict(self):
        my_model = BaseModel()
        model_dict = my_model.to_dict()

        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["created_at"], my_model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], my_model.updated_at.isoformat())

    def test_str(self):
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith("[BaseModel]"))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))

if __name__ == "__main__":
    unittest.main()
