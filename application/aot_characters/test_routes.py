import pytest
from . import routes
import sys
from unittest import mock
import requests
import os

def test_show_and_create():
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
