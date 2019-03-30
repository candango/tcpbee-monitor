from collections import namedtuple

Session = namedtuple("Session", [
    "type",
    "address",
    "port",
    "requests"
])

Request = namedtuple("Request", [
    "state",
    "time",
    "request_host",
    "target_host",
    "request_address",
    "request_data",
    "response_data",
    "elapsed_time"
])
