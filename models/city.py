#!/usr/bin/python3
"""
City Module

This module defines the City class, which represents a city entity. It inherits
from the BaseModel class.

Classes:
- City: Represents a city with various attributes.

Attributes:
- state_id (str): The ID of the state where the city is located.
- name (str): The name of the city.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from the BaseModel."""
    state_id = ''
    name = ''
