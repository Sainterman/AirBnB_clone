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

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_save(self):
        """
        Migoh no pleocuple
        """
        testinstance = BaseModel()
        testinstance.save()
        self.assertNotEqual(testinstance.created_at, testinstance.updated_at)
        self.assertIsInstance(testinstance.updated_at, datetime,
                              "updated_at is not instance of datetime.datetime")

    def test_to_dict(self):
        """
        checks if to_dict creates a dictionary
        """
        testinstance = BaseModel()
        self.assertIsInstance(testinstance.to_dict(), dict,
                              "to_dict methos doesnt returns dict obj")

    def test_str(self):
        """
        check if str complies to format
        """
        testinstance = BaseModel()
        a, b = testinstance.__class__.__name__, testinstance.id,
        c = testinstance.__dict__
        self.assertEqual("[{}] ({}) {}".format(a, b, c),
                         testinstance.__str__())


if __name__ == "__main__":
    unittest.main()
