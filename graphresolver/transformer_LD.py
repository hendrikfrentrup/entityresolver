import numpy as np
import pandas as pd
import graphresolver.record_schema

def clean_ip(ip_string):
    octet=(i for i in map(int,ip_string.split('.')))
    return '.'.join(map(str,octet))

class LDTransformer:

    def __init__(self):
        self.schema = graphresolver.record_schema.record_schema

        self.mapping=(  {"src_col":"Device Name",             "transformation":str.lower,      "dest_col":"hostname"},
                        {"src_col":"Type",                    "transformation":lambda x:x,     "dest_col":"device_type"},
                        {"src_col":"OS Name",                 "transformation":lambda x:x,     "dest_col":"os"},
                        {"src_col":"LDAP Name",               "transformation":lambda x:x,     "dest_col":"distinguished_name"},
                        {"src_col":"Address",                 "transformation":clean_ip,       "dest_col":"ip"},
                        {"src_col":"Last Hardware Scan Date", "transformation":pd.to_datetime, "dest_col":"last_scan_timestamp"},
                        {"src_col":"Serial Number",           "transformation":str.upper,      "dest_col":"serial_no"},
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
        self.output["source_name"]="LanDesk"
        self.unmapped_columns.discard("source_type")
        self.unmapped_columns.discard("source_name")

        # NaNs for unmapped columns
        for col in self.unmapped_columns:
            self.output[col]=np.NaN

    def load_csv_to_DataFrame(self, READ_FILE):
        print(f"reading {READ_FILE}")
        self.data = pd.read_csv(READ_FILE)

    def write_to_csv(self, WRITE_FILE):
        print(f"writing {WRITE_FILE}")
        self.output.to_csv(WRITE_FILE, sep=',')
