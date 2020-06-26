#!/usr/bin/python3
""" class BaseModel that defines
    all common attributes/methods
    for other classes:
"""
import uuid
from datetime import date


class BaseModel:
    """
    """
    id = ""

    def __init__(self):
        self.id = str(uuid.uuid4())
