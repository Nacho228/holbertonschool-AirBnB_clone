#!/usr/bin/python3
"""Unittest for City class"""
import unittest
from models.base_model import BaseModel
from models.city import City

city = City()
city.name = "Miami"
city.state_id = "6asdf453ghrny189d"


class TestCity(unittest.TestCase):
    """
    TestCity class to perform unit tests on the City class.
    """
    def test_subclass(self):
        """
        Test if City is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(city.__class__, BaseModel), True)

    def test_attr(self):
        """
        Test the attributes of City instance.
        """
        self.assertTrue("name" in city.__dict__)
        self.assertTrue("state_id" in city.__dict__)
        self.assertTrue("id" in city.__dict__)
        self.assertTrue("created_at" in city.__dict__)
        self.assertTrue("updated_at" in city.__dict__)

    def test_attr_type(self):
        """
        Test the attribute types of City instance.
        """
        self.assertEqual(type(city.name), str)
        self.assertEqual(type(city.state_id), str)

    def test_save(self):
        """
        Test the save() method of City instance.
        """
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict() method of City instance.
        """
        city_dict = city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
