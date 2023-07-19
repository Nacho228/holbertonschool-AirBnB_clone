#!/usr/bin/python3
"""
Amenity Module

This module defines the Amenity class, which represents a convenience or
service entity. It inherits from the BaseModel class.

Classes:
- Amenity: Represents an amenity with various attributes.

Attributes:
- name (str): The name of the amenity.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from the BaseModel."""
    name = ''
