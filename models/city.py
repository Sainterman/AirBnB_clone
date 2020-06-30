#!/usr/bin/python3
""" City class
"""
import models
from models.base_model import BaseModel


class City(BaseModel):
    """ A City Class that inherit from BaseModel
    """
    state_id = ""
    name = ""
