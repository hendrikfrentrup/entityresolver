import numpy as np
import pandas as pd
from graphresolver.generic_transformer import GenericTransformer

class ADTransformer(GenericTransformer):

    def __init__(self):
        super(ADTransformer, self).__init__()

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

        self.fill_unmapped_cols()

    def transform(self):
        super(ADTransformer, self).transform(source_name="ActiveDirectory", source_type="database")