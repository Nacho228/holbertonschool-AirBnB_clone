#!/usr/bin/python3
"""Unittest for Amenity class"""
import unittest
from models.base_model import BaseModel
from models.state import State

state = State()
state.name = "Florida"


class TestState(unittest.TestCase):
    """
    TestState class to perform unit tests on the State class.
    """
    def test_subclass(self):
        """
        Test if State is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(state.__class__, BaseModel), True)

    def test_attr(self):
        """
        Test the attributes of State instance.
        """
        self.assertTrue("id" in state.__dict__)
        self.assertTrue("created_at" in state.__dict__)
        self.assertTrue("updated_at" in state.__dict__)
        self.assertTrue("name" in state.__dict__)

    def test_attr_type(self):
        """
        Test the attribute types of State instance.
        """
        self.assertEqual(type(state.name), str)

    def test_save(self):
        """
        Test the save() method of State instance.
        """
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict() method of State instance.
        """
        state_dict = state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
