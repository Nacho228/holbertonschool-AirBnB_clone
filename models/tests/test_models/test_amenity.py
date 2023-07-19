#!/usr/bin/python3
"""Unittest for Amenity class"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

amenity = Amenity()
amenity.name = "Pool"


class TestAmenity(unittest.TestCase):
    """
    TestAmenity class to perform unit tests on the Amenity class.
    """
    def test_subclass(self):
        """
        Test that Amenity class is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(amenity.__class__, BaseModel), True)

    def test_attr(self):
        """
        Test that the necessary attributes are present in Amenity instance.
        """
        self.assertTrue("name" in amenity.__dict__)
        self.assertTrue("id" in amenity.__dict__)
        self.assertTrue("created_at" in amenity.__dict__)
        self.assertTrue("updated_at" in amenity.__dict__)

    def test_attr_type(self):
        """
        Test the attribute types of Amenity instance.
        """
        self.assertEqual(type(amenity.name), str)

    def test_save(self):
        """
        Test the save() method of Amenity instance.
        """
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict() method of Amenity instance.
        """
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
