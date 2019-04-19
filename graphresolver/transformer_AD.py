import numpy as np
import pandas as pd
import graphresolver.record_schema


class ADTransformer:

    def __init__(self):
        self.schema = graphresolver.record_schema.record_schema

        self.mapping=(  {"src_col":"Name",                            "transformation":str.lower,      "dest_col":"hostname"},
                        {"src_col":"Distinguished Name",              "transformation":lambda x:x,     "dest_col":"distinguished_name"},
                        {"src_col":"DNS Host Name",                   "transformation":str.lower,      "dest_col":"dns_name"},
                        {"src_col":"Operating System",                "transformation":lambda x:x,     "dest_col":"os"},
                        {"src_col":"Operating System Version Number", "transformation":lambda x:x,     "dest_col":"os_version"},
                        {"src_col":"Service Pack",                    "transformation":lambda x:x,     "dest_col":"os_service_pack"},
                        {"src_col":"Last Logon Date",                 "transformation":pd.to_datetime, "dest_col":"last_logon_timestamp"},
                        {"src_col":"Password Last Changed",           "transformation":pd.to_datetime, "dest_col":"last_pw_change_timestamp"},
                        {"src_col":"Creation Date",                   "transformation":pd.to_datetime, "dest_col":"first_seen_timestamp"},
        )

        self.mapped_columns=set()
        for col_op in self.mapping:
            self.mapped_columns.add(col_op["dest_col"])
        self.unmapped_columns=set(self.schema)-self.mapped_columns

    def transform(self):
        # TODO: make sure a DataFrame is loaded into self.data
        self.output=pd.DataFrame()
        for col_op in self.mapping:
            self.output[col_op["dest_col"]] = self.data[col_op["src_col"]].apply(col_op["transformation"])
        
        # assign source name & source type
        self.output["source_type"]="database"
        self.output["source_name"]="ActiveDirectory"
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