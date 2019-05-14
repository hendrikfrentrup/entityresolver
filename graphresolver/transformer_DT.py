import numpy as np
import pandas as pd
from graphresolver.generic_transformer import GenericTransformer

class DTTransformer(GenericTransformer):

    def __init__(self):
        super(DTTransformer, self).__init__()

        self.mapping=(  {"src_col":"Hostname2",       "transformation":str.lower,      "dest_col":"hostname"},
                        {"src_col":"Type",            "transformation":lambda x:x,     "dest_col":"device_type"},
                        {"src_col":"MacAddress",      "transformation":lambda x:x,     "dest_col":"mac"},
                        {"src_col":"Hostname",        "transformation":str.lower,      "dest_col":"dns_name"},
                        {"src_col":"OperatingSystem", "transformation":lambda x:x,     "dest_col":"os"},
                        {"src_col":"FirstSeen",       "transformation":pd.to_datetime, "dest_col":"first_seen_timestamp"},
                        {"src_col":"LastSeen",        "transformation":pd.to_datetime, "dest_col":"last_seen_timestamp"},
        )

        self.fill_unmapped_cols()

def transform(self):
        super(DTTransformer, self).transform(source_name="DarkTrace", source_type="network_scan")
