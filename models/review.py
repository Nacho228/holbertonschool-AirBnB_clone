#!/usr/bin/python3
"""
Review Module

This module defines the Review class, which represents a review entity. It
inherits from the BaseModel class.

Classes:
- Review: Represents a review entity with place_id, user_id,
and text attributes.

Attributes:
- place_id (str): The ID of the place associated with the review.
- user_id (str): The ID of the user who created the review.
- text (str): The text content of the review.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from the BaseModel."""
    place_id = ''
    user_id = ''
    text = ''
