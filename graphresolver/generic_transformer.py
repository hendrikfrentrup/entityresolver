import numpy as np
import pandas as pd
import graphresolver.record_schema


class GenericTransformer(object):

    def __init__(self):
        self.schema = graphresolver.record_schema.record_schema
    
    def fill_unmapped_cols(self):
        self.mapped_columns=set()
        for col_op in self.mapping:
            self.mapped_columns.add(col_op["dest_col"])
        self.unmapped_columns=set(self.schema)-self.mapped_columns

    def transform(self, source_name, source_type):
        # TODO: make sure a DataFrame is loaded into self.data
        self.output=pd.DataFrame()
        for col_op in self.mapping:
            self.output[col_op["dest_col"]] = self.data[col_op["src_col"]].apply(col_op["transformation"])
        
        # assign source name & source type
        self.output["source_type"]=source_type
        self.output["source_name"]=source_name
        self.unmapped_columns.discard("source_type")
        self.unmapped_columns.discard("source_name")

        # NaNs for unmapped columns
        for col in self.unmapped_columns:
            self.output[col]=np.NaN


    # TODO: another set of IO methods - these are only to be used 
    # temporarily and a more permanent read-write tool needs 
    # to be employed here. Pandas has its own IO csv import here, 
    # so no extra dependency

    def load_csv_to_DataFrame(self, READ_FILE):
        print(f"reading {READ_FILE}")
        self.data = pd.read_csv(READ_FILE)

    def write_to_csv(self, WRITE_FILE):
        print(f"writing {WRITE_FILE}")
        self.output.to_csv(WRITE_FILE, sep=',')