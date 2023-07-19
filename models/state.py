#!/usr/bin/python3
"""
State Module

This module defines the State class, which represents a state entity. It
inherits from the BaseModel class.

Classes:
- State: Represents a state entity with a name attribute.

Attributes:
- name (str): The name of the state.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from the BaseModel."""
    name = ''
