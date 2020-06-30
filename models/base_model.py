#!/usr/bin/python3

""" class BaseModel that defines
    all common attributes/methods
    for other classes:
"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """
    """
    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            for pair in kwargs.items():
                if pair[0] == 'created_at' or pair[0] == 'updated_at':
                    date = datetime.strptime(pair[1],'%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, pair[0], date)
                elif pair[0] == '__class__':
                    pass
                else:
                    setattr(self, pair[0], pair[1])

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        a, b, c = self.__class__.__name__, self.id, self.__dict__
        return "[{}] ({}) {}".format(a, b, c)

    def to_dict(self):
        """ Returns a dictionary containing all
            keys/values of __dict__ of the instance:
        """
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.__dict__['created_at'].isoformat()
        new_dict["updated_at"] = self.__dict__['updated_at'].isoformat()
        return new_dict
