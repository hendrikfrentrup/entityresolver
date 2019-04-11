#!/usr/bin/env python

import os
import argparse
import csv
import networkx as nx


class nxResolver:

    def __init__(self):
        self.G = nx.Graph()

    def get_graph_stats(self):
        n = self.G.number_of_nodes()
        e = self.G.number_of_edges()
        return n, e

    def create_nodes_from_dict(self, record_dict):
        n_nodes=0
        for i, record in record_dict.items():
            self.G.add_node(i,  ip=record['ip'], 
                                mac=record['mac'], 
                                hostname=record['hostname'], 
                                serial_no=record['mac'],
                                source=record['source']
                            )
            n_nodes+=1
        print(f"{n_nodes} nodes added to graph.")


    def generate_edges(self):
        # make sure there are nodes loaded
        g=self.G
        n_comparisons=0
        n_edges=0

        for i in g.nodes:
            # TODO: only need to count from r-t, halves the loop
            for j in g.nodes:
                n_comparisons+=1
                edge_flag=False
                if i!=j:
                    #TODO: iterate through columns to match
                    if (g.node[i]['ip']!='') & (g.node[i]['ip']==g.node[j]['ip']):
                        edge_flag=True
                    elif (g.node[i]['mac']!='') & (g.node[i]['mac']==g.node[j]['mac']):
                        edge_flag=True
                    elif (g.node[i]['hostname']!='') & (g.node[i]['hostname']==g.node[j]['hostname']):
                        edge_flag=True
                    elif (g.node[i]['serial_no']!='') & (g.node[i]['serial_no']==g.node[j]['serial_no']):
                        edge_flag=True
                        
                    if edge_flag:
                        n_edges+=1
                        g.add_edge(i,j)
                        # TODO: add an edge type, e.g. ip-match/mac-match
        print(f"{n_edges} edges created, out of a possible {n_comparisons}")

    def compute_connComponents(self):
        pass

    def generate_taggedDict(self):
        pass


def csv2dict(csv_file):
    out_dict={}
    with open(csv_file) as csv_records:
        reader = csv.DictReader(csv_records)
        for i,row in enumerate(reader):
            out_dict[i]=row
    return out_dict

def dict2csv(out_file):
    pass

def main():
    # read csv filename from args
    parser = argparse.ArgumentParser(description='graph-based Entity Resolution via networkx')
    parser.add_argument('-f', '--file', dest='csv_file', help='provide CSV file of records (with one header line) ')
    args = parser.parse_args()

    if args.csv_file:
        if os.path.isfile(args.csv_file):
            records = csv2dict(args.csv_file)

            resolver = nxResolver()
            resolver.create_nodes_from_dict(records)
            resolver.generate_edges()
            
            n, e = resolver.get_graph_stats()
            print(f"currently in graph: {n} nodes, {e} edges")
        
        else:
            print("File not found.")
    else:
        print("No useful argument given. Get help with option -h/--help.")

    # TODO: add cmdline arg to specify which cols to match on and ignore the rest

    # attempt loading csv file
    # call csv2dict to generate dict of parsed records
    # instaitate nxResolver
    # create edges from dict
    # compute CCs
    # generate a dict of tagged records
    # export as csv through dict2csv
    print("Done!")

if __name__ == "__main__":
    main()
