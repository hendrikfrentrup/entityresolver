import numpy as np
import pandas as pd
from graphresolver.generic_transformer import GenericTransformer

def clean_ip(ip_string):
    octet=(i for i in map(int,ip_string.split('.')))
    return '.'.join(map(str,octet))

class LDTransformer(GenericTransformer):

    def __init__(self):
        super(LDTransformer, self).__init__()

        self.mapping=(  {"src_col":"Device Name",             "transformation":str.lower,      "dest_col":"hostname"},
                        {"src_col":"Type",                    "transformation":lambda x:x,     "dest_col":"device_type"},
                        {"src_col":"OS Name",                 "transformation":lambda x:x,     "dest_col":"os"},
                        {"src_col":"LDAP Name",               "transformation":lambda x:x,     "dest_col":"distinguished_name"},
                        {"src_col":"Address",                 "transformation":clean_ip,       "dest_col":"ip"},
                        {"src_col":"Last Hardware Scan Date", "transformation":pd.to_datetime, "dest_col":"last_scan_timestamp"},
                        {"src_col":"Serial Number",           "transformation":str.upper,      "dest_col":"serial_no"},
        )

        self.fill_unmapped_cols()

def transform(self):
        super(LDTransformer, self).transform(source_name="LanDesk", source_type="database")
