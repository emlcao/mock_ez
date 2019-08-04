#!/usr/bin/env python

"""
Tests for the mock_ez.get_webpage module
"""

import unittest
import mock
from mock_ez import flower_type


class TestGetWebPage(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # Configure mock object for requests.get
        cls.mock_get_patcher = mock.patch('requests.get')
        cls.mock_rg = cls.mock_get_patcher.start()

        # Set up Mock object response
        from requests.models import Response
        cls.mock_rg.return_value = mock.Mock(spec=Response)
        cls.mock_rg.return_value.status_code = 200

    def test_fetch_a_status_code(self):
        pass


if __name__ == '__main__':
    unittest.main()
