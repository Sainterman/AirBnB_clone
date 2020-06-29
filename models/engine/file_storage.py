#!/usr/bin/python3
"""
"""
import json
import models
from os import path


class FileStorage:
    """ Private class attributes for class FileStorage
    """
    __file_path = "file.json"
    __objects = {}
    def __init__():
        pass
    
    def all(self):
        """ Returns the dictionary with objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Return __objects with obj set as key
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path)
        """
        save_file = json.__file_path
        new_dict = {}
        for item in self.__objects.items():
            new_dict[item] = item.to_dict()
        with open("save_file", mode="w", encoding="utf-8") as new_file:
            json.dump(new_dict, new_file)

    def reload(self):
        """ Deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists;
            otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised)
        """
        Reload_dict = {}

