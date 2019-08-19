#!/usr/bin/env python
import requests

class GetWebPage(object):
    def __init__(self, user=None):
        self.user = user

    @staticmethod
    def fetch_a_status_code(url):
        """
        Fetch response from a webpage
        Assumption: No username and password needed to fetch information
        """
        res = requests.get(url)
        return res.status_code
