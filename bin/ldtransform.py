#!/usr/bin/env python

import argparse
import os

from graphresolver.transformer_LD import LDTransformer

def main():
    # read csv filename from args
    parser = argparse.ArgumentParser(description='map & clean LanDesk CSV export')
    parser.add_argument('-i', '--input', dest='READ_FILE', help='provide CSV file of LD records (with one header line) ')
    parser.add_argument('-o', '--output', dest='WRITE_FILE', help='CSV file with mapped & cleaned records to be written.')
    args = parser.parse_args()

    if args.READ_FILE and args.WRITE_FILE:
        if os.path.isfile(args.READ_FILE):
            tf = LDTransformer()
            tf.load_csv_to_DataFrame(args.READ_FILE)
            tf.transform()
            tf.write_to_csv(args.WRITE_FILE)
        else:
            print(f"Input CSV File not found: {args.READ_FILE}")

    else:
        print("""No useful arguments given. Specify an input and output file!
                 Get help with option -h/--help.""")

if __name__ == "__main__":
    main()

