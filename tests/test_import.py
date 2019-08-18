#!/usr/bin/env python
"""
Tests for the mock_ez.mock_ez module
"""

import unittest


class TestImport(unittest.TestCase):
    def test__module__import(self):
        import mock_ez


if __name__ == '__main__':
    unittest.main()
