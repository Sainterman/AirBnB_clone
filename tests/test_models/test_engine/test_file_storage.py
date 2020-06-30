#!/usr/bin/python3

"""
unittests for the file storage class
"""

import unittest
import pep8
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for FileStorage Class including style
    test return eload and save
    """

    def SetUp(self):
        """reset instances, clean file.json maybe"""
        pass

    def test_pep8_style(self):
        """ Check pep8 style"""
        basePep8Style = pep8.StyleGuide(quiet=True)
        result = basePep8Style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(result.total_errors, 0, "base file has pep8 errors")


if __name__ == "__main__":
    unittest.main()
