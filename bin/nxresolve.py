#!/usr/bin/env python

import argparse
import os

from graphresolver.nxResolver import nxResolver
from graphresolver.nxResolver import csv2dict, records2csv

def main():
    # read csv filename from args
    parser = argparse.ArgumentParser(description='graph-based Entity Resolution via networkx')
    parser.add_argument('-f', '--file', dest='csv_file', help='provide CSV file of records (with one header line) ')
    parser.add_argument('-o', '--output', dest='out_file', help='''CSV file with tagged records to be written. 
                                                                   If not specified, written to resolved_records.csv by default''')
    args = parser.parse_args()

    if args.csv_file:
        if os.path.isfile(args.csv_file):
            # call csv2dict to generate dict of parsed records
            records = csv2dict(args.csv_file)

            # instiatate nxResolver
            resolver = nxResolver()
            resolver.create_nodes_from_dict(records)
            # create edges from dict
            resolver.generate_edges()
            
            n, e = resolver.get_graph_stats()
            print(f"currently in graph: {n} nodes, {e} edges")

            # compute CCs
            resolver.generate_conncomponents()

            # generate a list of tagged records & export as csv
            if args.out_file:
                records2csv(resolver.tagged_records, out_file=args.out_file)
            else:
                records2csv(resolver.tagged_records)
        
        else:
            print("File not found.")
    else:
        print("No useful argument given. Get help with option -h/--help.")

    # TODO: add cmdline arg to specify which cols to match on and ignore the rest

    print("Done!")

if __name__ == "__main__":
    main()