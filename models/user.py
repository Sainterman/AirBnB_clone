#!/usr/bin/python3
""" Class Users
"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """ A User Class that inherit from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
