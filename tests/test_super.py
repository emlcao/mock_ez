#!/usr/bin/env python
import unittest
import mock

class TestSuper(unittest.TestCase):
    @classmethod
    def setUp(cls):
        from mock_ez.get_square import Rectangle, Square, Cube

    def tearDown(cls):
        pass

    def test_square_class(self):
        pass

    def test_cube(self):
        pass



if __name__ == '__main__':
    unittest.main()
