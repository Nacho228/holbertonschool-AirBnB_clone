#!/usr/bin/python3
"""Unittest for User class"""
import unittest
from models.base_model import BaseModel
from models.user import User

user = User()
user.email = "lorem@ipsum.com"
user.first_name = "Jimmy"
user.last_name = "Buckets"
user.password = "im_HIM"


class TestUser(unittest.TestCase):
    """
    TestUser class to perform unit tests on the User class.
    """
    def test_subclass(self):
        """
        Test if User is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(user.__class__, BaseModel), True)

    def test_attr(self):
        """
        Test the attributes of User instance.
        """
        self.assertTrue("email" in user.__dict__)
        self.assertTrue("password" in user.__dict__)
        self.assertTrue("first_name" in user.__dict__)
        self.assertTrue("last_name" in user.__dict__)
        self.assertTrue("id" in user.__dict__)
        self.assertTrue("created_at" in user.__dict__)
        self.assertTrue("updated_at" in user.__dict__)

    def test_attr_type(self):
        """
        Test the attribute types of User instance.
        """
        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)
        self.assertEqual(type(user.password), str)

    def test_save(self):
        """
        Test the save() method of User instance.
        """
        user.save()
        self.assertNotEqual(user.created_at, user.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict() method of User instance.
        """
        user_dict = user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
