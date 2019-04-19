import unittest
import graphresolver.record_schema


class test_nxResolver(unittest.TestCase):

    def test_schema(self):
        schema=graphresolver.record_schema.record_schema
        target_schema=(
                        "record_id",  
                        "serial_no",
                        "hostname", 
                        "mac",
                        "ip",
                        "dns_name",
                        "distinguished_name",
                        "device_type",
                        "os_type",
                        "os",
                        "os_version",
                        "os_service_pack",
                        "user",
                        "last_logon_timestamp",
                        "last_pw_change_timestamp",
                        "owner",
                        "first_seen_timestamp",
                        "last_seen_timestamp",
                        "last_scan_timestamp",
                        "source_type",
                        "source_name"
        )

        for e in schema:
            assert e in target_schema