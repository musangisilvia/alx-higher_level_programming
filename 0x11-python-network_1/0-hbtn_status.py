#!/usr/bin/python3
"""
    A script that fetches https://intranet.htbn.io/status
"""


import urllib.request


with urllib.request.urlopen('https://intranet.htbn.io/status') as resp:
    page = resp.read()
