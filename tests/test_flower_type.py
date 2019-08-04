#!/usr/bin/env python
"""
Tests for the mock_ez.mock_ez module
"""

import unittest

class TestFlowerType(unittest.TestCase):
    def test_rose_type(self):
        from mock_ez import flower_type
        t = flower_type.FlowerType('red', 11)
        res = t.flower_type()
        exp_res = 'rose'
        self.assertEqual(res, exp_res)


if __name__ == '__main__':
    unittest.main()
