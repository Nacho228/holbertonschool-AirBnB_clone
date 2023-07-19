#!/usr/bin/python3
"""Unittest for BaseModel class"""
import unittest
from models.base_model import BaseModel

base = BaseModel()


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel class to perform unit tests on the BaseModel class.
    """
    def test_init(self):
        """
        Test the initialization of BaseModel instance.
        """
        self.assertTrue(isinstance(base, BaseModel))

    def test_save(self):
        """
        Test the save() method of BaseModel instance.
        """
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict() method of BaseModel instance.
        """
        base_dict = base.to_dict()
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertIsInstance(base_dict["created_at"], str)
        self.assertIsInstance(base_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
