import os
import sys

from pbx_gs_python_utils.utils.Dev import Dev

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import unittest
from graphresolver.nxResolver import nxResolver

class test_nxResolver(unittest.TestCase):

    def setUp(self):
        self.resolver = nxResolver()

    def test__init__(self):
        assert type(self.resolver).__name__ == 'nxResolver'

#    def test_create_edges_from_dict(self):
#        assert self.resolver.create_edges_from_dict() == None
