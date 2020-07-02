#!/usr/bin/python3
""" Review class
"""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """ A Review Class that inherit from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
