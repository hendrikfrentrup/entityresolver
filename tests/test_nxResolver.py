import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import unittest
from graphresolver.nxResolver import nxResolver

class test_nxResolver(unittest.TestCase):

    def setUp(self):
        self.resolver = nxResolver()

    def test_create_edges_from_dict(self):
        assert self.resolver.create_edges_from_dict() == None
