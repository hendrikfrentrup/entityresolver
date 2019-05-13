import numpy as np
import pandas as pd
from graphresolver.generic_transformer import GenericTransformer

class SYTransformer(GenericTransformer):

    def __init__(self):
        super(SYTransformer, self).__init__()

        self.mapping=(  {"src_col":"Hardware Serial Number",  "transformation":str.upper,      "dest_col":"serial_no"},
                        {"src_col":"Computer Name",           "transformation":str.lower,      "dest_col":"hostname"},
                        {"src_col":"Operating System",        "transformation":lambda x:x,     "dest_col":"os"},
                        {"src_col":"Kernel",                  "transformation":lambda x:x,     "dest_col":"os_version"},
                        {"src_col":"Last Scan Time",          "transformation":pd.to_datetime, "dest_col":"last_scan_timestamp"},
                        {"src_col":"Last time status changed","transformation":pd.to_datetime, "dest_col":"last_seen_timestamp"},
                        {"src_col":"Current User",            "transformation":lambda x:x,     "dest_col":"user"},
        )

        self.fill_unmapped_cols()

def transform(self):
        super(SYTransformer, self).transform(source_name="Symantec-SEP", source_type="endpoint_agent")
