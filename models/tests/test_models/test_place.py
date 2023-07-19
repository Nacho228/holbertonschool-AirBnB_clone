#!/usr/bin/python3
"""Unittest for Place class"""
import unittest
from models.base_model import BaseModel
from models.place import Place

place = Place()
place.name = "Big Face Hotel"
place.description = "Very nice hotel"
place.city_id = "6qwef516t4df615"
place.user_id = "9fg8h7fsh123ads"
place.number_rooms = 20
place.number_bathrooms = 40
place.max_guest = 200
place.price_by_night = 1000
place.latitude = 165.654318
place.longitude = -16.684638
place.amenity_ids = []


class TestPlace(unittest.TestCase):
    """
    TestPlace class to perform unit tests on the Place class.
    """
    def test_subclass(self):
        """
        Test if Place is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(place.__class__, BaseModel), True)

    def test_attr(self):
        """
        Test the attributes of Place instance.
        """
        self.assertTrue("city_id" in place.__dict__)
        self.assertTrue("user_id" in place.__dict__)
        self.assertTrue("name" in place.__dict__)
        self.assertTrue("description" in place.__dict__)
        self.assertTrue("number_rooms" in place.__dict__)
        self.assertTrue("number_bathrooms" in place.__dict__)
        self.assertTrue("max_guest" in place.__dict__)
        self.assertTrue("price_by_night" in place.__dict__)
        self.assertTrue("latitude" in place.__dict__)
        self.assertTrue("longitude" in place.__dict__)
        self.assertTrue("amenity_ids" in place.__dict__)
        self.assertTrue("id" in place.__dict__)
        self.assertTrue("created_at" in place.__dict__)
        self.assertTrue("updated_at" in place.__dict__)

    def test_attr_type(self):
        """
        Test the attribute types of Place instance.
        """
        self.assertEqual(type(place.city_id), str)
        self.assertEqual(type(place.user_id), str)
        self.assertEqual(type(place.name), str)
        self.assertEqual(type(place.description), str)
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(type(place.amenity_ids), list)

    def test_save(self):
        """
        Test the save() method of Place instance.
        """
        place.save()
        self.assertNotEqual(place.created_at, place.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict() method of Place instance.
        """
        place_dict = place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertIsInstance(place_dict["created_at"], str)
        self.assertIsInstance(place_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
