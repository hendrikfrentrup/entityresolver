#!/usr/bin/env python

import argparse
import os

from graphresolver.nxResolver import nxResolver
from graphresolver.nxResolver import csv2dict

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

            resolver.generate_conncomp_as_dict()
        
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