#!/usr/bin/python3
""" class BaseModel that defines
    all common attributes/methods
    for other classes:
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        self.updated_at = datetime.now()
