record_schema=(
   "record_id",  # unique identifier to source record (e.g. hash of the source)
   "serial_no", # -> upper()
   "hostname", # -> upper()
   "mac",  # -> 00:00:00:00
   "ip",  # -> (:d).(:d).(:d).(:d)
   "dns_name",  # aka fqdn -> lower
   "distinguished_name",  # aka "CN=.., OU=.." or "<cn>/<ou>/<dc>"
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