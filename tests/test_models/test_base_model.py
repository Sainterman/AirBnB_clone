#!/usr/bin/python3
""" Test for class BaseModel
"""

import unittest
import pep8
from datetime import datetime
from models.base_model import BaseModel
import models


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
        self.assertIsInstance(testinstance.id, str, "id is not a string")

    def test_created_at(self):
        """Verify if is instance"""
        testinstance = BaseModel()
        self.assertIsInstance(testinstance.created_at, datetime,
                              "create_at is not instance of datetime.datetime")

    def test_str(self):
        """Verifies number"""
        testinstance = BaseModel()
        testinstance.name = "Holberton"
        testinstance.my_number = 89

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

if __name__ == "__main__":
    unittest.main()
