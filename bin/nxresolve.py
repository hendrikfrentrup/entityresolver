#!/usr/bin/env python

import argparse
import os

from graphresolver.nxResolver import nxResolver
from graphresolver.nxResolver import csv2dict, records2csv

def main():
    # read csv filename from args
    parser = argparse.ArgumentParser(description='graph-based Entity Resolution via networkx')
    parser.add_argument('-f', '--file', dest='csv_file', help='provide CSV file of records (with one header line) ')
    parser.add_argument('-t', '--tagged', dest='tagged_file', help='CSV file with tagged records to be written.')
    parser.add_argument('-m', '--merged', dest='merged_file', help='CSV file with merged entities to be written.')
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
            msg = resolver.generate_conncomponents()
            print(msg)

            msg = resolver.merge_records()
            print(msg)        
        else:
            print(f"Input CSV File not found: {args.csv_file}")
    else:
        print("No useful argument given. Get help with option -h/--help.")

    # generate a list of tagged records/merged entities & export as csv
    if args.tagged_file:
        records2csv(resolver.tagged_records, out_file=args.tagged_file)
        print(f"records tagged in {args.tagged_file}.")
    else:
        print("No output file specified to produce tagged records")

    if args.merged_file:
        records2csv(resolver.consolidated_entities, out_file=args.merged_file)
        print(f"entities merged in {args.merged_file}.")
    else:
        print("No output file specified to produce merged entities")

    # TODO: add cmdline arg to specify which cols to match on and ignore the rest

    print("Done!")

if __name__ == "__main__":
    main()