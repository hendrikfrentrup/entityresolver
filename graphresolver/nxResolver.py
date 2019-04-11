#!/usr/bin/env python

import os
import argparse
import csv
import networkx as nx


class nxResolver:

    def __init__(self):
        pass

    def create_edges_from_dict(self):
        return None

    def compute_connComponents(self):
        pass

    def generate_taggedDict(self):
        pass


def csv2dict(csv_file):
    out_dict={}
    with open(csv_file) as csv_records:
        reader = csv.DictReader(csv_records)
        for i,row in enumerate(reader):
            print(row)
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
