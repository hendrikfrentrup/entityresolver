import unittest
from graphresolver.transformer_AD import ADTransformer
from graphresolver.record_schema import record_schema

class test_ADTransformer(unittest.TestCase):

    def setUp(self):
        self.transformer = ADTransformer()

    def test__init__(self):
        assert set() == self.transformer.mapped_columns.intersection(self.transformer.unmapped_columns)
        for field in record_schema:
            assert field in tuple(self.transformer.mapped_columns.union(self.transformer.unmapped_columns))
        for el in self.transformer.mapping:
            keys=el.keys()
            assert len(keys) == 3
            assert "src_col" in keys
            assert "dest_col" in keys
            assert "transformation" in keys

    def test_transform(self):
        pass