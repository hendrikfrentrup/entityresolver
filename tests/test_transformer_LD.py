import unittest
from graphresolver.transformer_LD import LDTransformer
from graphresolver.transformer_LD import clean_ip

class test_LDTransformer(unittest.TestCase):

    def setUp(self):
        self.transformer = LDTransformer()

    def test__init__(self):
        pass
        # assert self.transformer

    def test_clean_ip(self):
        input = "010.016.050.012"
        cleaned_input = clean_ip(input)
        assert cleaned_input == "10.16.50.12"