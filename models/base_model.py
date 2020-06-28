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

    def __str__(self):
        a, b, c = self.__class__.__name__, self.id, self.__dict__
        return "[{}] ({}) {}".format(a, b, c)

    def to_dict(self):
        """ Returns a dictionary containing all
            keys/values of __dict__ of the instance:
        """
        new_dict = self.__dict__
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    
