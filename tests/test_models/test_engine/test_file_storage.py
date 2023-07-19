#!/usr/bin/python3
"""Unittest for FileStorage class"""
import unittest
import os
from models.user import User
from models.engine.file_storage import FileStorage

storage = FileStorage()
user = User()
user.email = "HIM@Heat.com"
user.first_name = "Jimmy"
user.last_name = "Buckets"
user.password = "im_HIM"
storage.save()


class TestFileStorage(unittest.TestCase):
    """
    TestFileStorage class to perform unit tests on the FileStorage class.
    """
    def test_all(self):
        """
        Test the all() method of FileStorage.
        """
        obj_dict = storage.all()
        self.assertIsNotNone(obj_dict)
        self.assertIsInstance(obj_dict, dict)

    def test_new(self):
        """
        Test the new() method of FileStorage.
        """
        obj_dict = storage.all()
        storage.new(user)
        key = f"{user.__class__.__name__}.{user.id}"
        self.assertIsNotNone(obj_dict[key])

    def test_save(self):
        """
        Test the save() method of FileStorage.
        """
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """
        Test the reload() method of FileStorage.
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as f:
            for arg in f:
                self.assertEqual(arg, "{}")
        self.assertIs(storage.reload(), None)

    def test_file_path(self):
        """
        Test the file_path attribute of FileStorage.
        """
        self.assertTrue(type(storage._FileStorage__file_path) is str)

    def test_objs_dict(self):
        """
        Test the __objects attribute of FileStorage.
        """
        self.assertTrue(type(storage._FileStorage__objects) is dict)


if __name__ == "__main__":
    unittest.main()
