#!/usr/bin/python3
"""
aqui williyrex comentando
"""
import json


class FileStorage:
    """ Private class attributes for class FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary with objects
        """
        return type(self)._objects

    def new(self, obj):
        """ Return __objects with obj set as key
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
        return "OK"


    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path)
        """
        save_file = self.__file_path
        new_dict = {}
        for item in type(self).__objects.items():
            new_dict[item[0]] = item[1].to_dict()

        with open(type(self).__file_path, mode="w", encoding="utf-8") as nf:
            json.dump(new_dict, nf)
        return "OK"

    def reload(self):
        """ Deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists;
            otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised)
        """
        Reload = {}
        try:
            with open(type(self).__file_path, mode='r') as f:
                Reload = json.load(f)
                for key, value in Reload.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        except:
            pass

