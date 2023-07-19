#!/usr/bin/python3
"""Unittest for Amenity class"""
import unittest
from models.base_model import BaseModel
from models.review import Review

review = Review()
review.place_id = "k6fhyu16a5sdg1"
review.user_id = "cv16jdyer6a4y1d"
review.text = "Lorem ipsum"


class TestReview(unittest.TestCase):
    """
    TestReview class to perform unit tests on the Review class.
    """
    def test_subclass(self):
        """
        Test if Review is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(review.__class__, BaseModel), True)

    def test_attr(self):
        """
        Test the attributes of Review instance.
        """
        self.assertTrue("id" in review.__dict__)
        self.assertTrue("created_at" in review.__dict__)
        self.assertTrue("updated_at" in review.__dict__)
        self.assertTrue("place_id" in review.__dict__)
        self.assertTrue("user_id" in review.__dict__)
        self.assertTrue("text" in review.__dict__)

    def test_attr_type(self):
        """
        Test the attribute types of Review instance.
        """
        self.assertEqual(type(review.place_id), str)
        self.assertEqual(type(review.user_id), str)
        self.assertEqual(type(review.text), str)

    def test_save(self):
        """
        Test the save() method of Review instance.
        """
        review.save()
        self.assertNotEqual(review.created_at, review.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict() method of Review instance.
        """
        review_dict = review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
