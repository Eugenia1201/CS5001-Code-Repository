"""This is the module for unittesting for "Into the seaworld" program"""

import unittest
import seaworld_configui as sc
# from unittest.mock import patch
# from unittest.mock import Mock


class Test_StringConvert(unittest.TestCase):
    def test_valid_int_conversion(self):
        r = sc.InputCheck()
        self.assertEqual(r.number_or_none("100"), 100,
                         "String 100 should be converted into integer 100")

    def test_invalid_int_conversion(self):
        r = sc.InputCheck()
        self.assertIsNone(r.number_or_none("not a number"),
                          "Invalid input should return None")

    def test_valid_float_conversion(self):
        r = sc.InputCheck()
        self.assertEqual(r.float_or_none("1.24"), 1.24,
                         "String 1.45 should be converted to float 1.24")

    def test_invalid_float_conversion(self):
        r = sc.InputCheck()
        self.assertIsNone(r.float_or_none("not a number"),
                          "Invalid input should return None")


if __name__ == "__main__":
    unittest.main()
