#!/usr/bin/python3
"""
This module provides a FileStorage class that serializes instances
to a JSON file and deserializes JSON files to instances.

Classes:
FileStorage: The main class that handles serialization and deserialization.

Methods:
- all: Returns the dictionary __objects.
- new: Sets in __objects the obj with key <obj class name>.id.
- save: Serializes __objects to the JSON file (path: __file_path).
- reload: Deserializes the JSON file to __objects.
"""
import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "City": City,
                  "State": State, "Amenity": Amenity,
                  "Review": Review, "Place": Place}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        if FileStorage.__objects is not None:
            objs_to_dump = {}
            for k, v in FileStorage.__objects.items():
                objs_to_dump[k] = v.to_dict()
            with open(FileStorage.__file_path, "w") as f:
                json.dump(objs_to_dump, f)

    def reload(self):
        """
         Deserializes the JSON file to __objects (only if the
         JSON file (__file_path) exists ; otherwise, do nothing.
         If the file doesn't exist, no exception should be raised)
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                new_obj = json.load(f)
            for k, v in new_obj.items():
                obj = FileStorage.class_dict[v["__class__"]](**v)
                FileStorage.__objects[k] = obj
