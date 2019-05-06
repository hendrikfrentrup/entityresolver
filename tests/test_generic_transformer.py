import unittest
from graphresolver.transformer_AD import GenericTransformer
from graphresolver.record_schema import record_schema

class test_GenericTransformer(unittest.TestCase):

    def setUp(self):
        self.transformer = GenericTransformer()

    def test__init__(self):
        assert self.transformer.schema == record_schema
    
    #TODO: 
    # def test_fill_unmapped_cols
    # def test_transform
