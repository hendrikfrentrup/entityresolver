from graphresolver.Data_CSV import Data_CSV
import unittest
from graphresolver.nxResolver import nxResolver

class test_nxResolver(unittest.TestCase):

    def setUp(self):
        self.resolver = nxResolver()
        self.graph    = self.resolver.G

    def test__init__(self):
        assert type(self.resolver).__name__   == 'nxResolver'
        assert type(self.resolver.G).__name__ == 'Graph'

    def test_get_graph_stats(self):
        (nodes,edges) = self.resolver.get_graph_stats()
        assert nodes == 0
        assert edges == 0
        self.graph.add_node('asd')
        self.graph.add_edge('from','to')
        (nodes, edges) = self.resolver.get_graph_stats()
        assert nodes == 3
        assert edges == 1

    def test_create_nodes_from_dict(self):

        assert self.resolver.create_nodes_from_dict({})          == '0 nodes added to graph.'

        record_dict = {'node_1': {  'ip'         : 'ip'      ,
                                    'mac'       : 'mac'     ,
                                    'hostname'   : 'hostname',
                                    'serial_no'  :'serial_no',
                                    'source'     :'source'   } }
        assert self.resolver.create_nodes_from_dict(record_dict) == '1 nodes added to graph.'
        assert self.graph.nodes._nodes == record_dict

    def test_generate_edges(self):
        assert self.resolver.generate_edges() == '0 edges created, out of a possible 0'

        data = Data_CSV().csv_2_dict('Resolver_Data.csv')
        self.resolver.create_nodes_from_dict(data)
        assert self.resolver.generate_edges() == '6 edges created, out of a possible 16'

    def test_tag_node_as_dict(self):
        record_dict = {99: { 'ip': 'ip',
                            'mac': 'mac',
                            'hostname': 'hostname',
                            'serial_no': 'serial_no',
                            'source': 'source'} }

        self.resolver.create_nodes_from_dict(record_dict)

        out_dict = {'entity_id': 0}
        for k,v in record_dict[99].items(): out_dict[k]=v
                                                                         
        assert self.resolver.tag_node_as_dict(0, self.graph.node[99]) == out_dict

    def test_generate_conncomponents(self):
        data = Data_CSV().csv_2_dict('Tiny_Test_Data.csv')
        self.resolver.create_nodes_from_dict(data)

        assert self.resolver.generate_edges() == '6 edges created, out of a possible 36'
        assert self.resolver.generate_conncomponents() == '6 records tagged with 3 entities'