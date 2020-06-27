#!/usr/bin/python3
""" Test for class BaseModel
"""
import unittest
import pep8
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ Test case for BaseModel, include
        style and id.
    """
    def test_pep8style(self):
        """ verify style pep8
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_id(self):
        """ Verify that id is a string
        """
        testinstance = BaseModel()
        print("BaseModel id: {}".format(testinstance.id))
        self.assertIsInstance(testinstance.id, str, "id is not a string")

    def test_created_at(self):
        testinstance = BaseModel()
        self.assertIsInstance(testinstance.created_at, datetime,
                              "create_at is not instance of datetime.datetime")

if __name__ == "__main__":
    unittest.main()