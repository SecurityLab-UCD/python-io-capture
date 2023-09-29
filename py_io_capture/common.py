import os
from strenum import StrEnum

MAX_REPORT_SIZE = int(os.getenv("MAX_REPORT_SIZE", 10))
DUMP_FILE_NAME = os.getenv("DUMP_FILE_NAME", "py_io_capture_report.json")
MAX_RECURRSION_LIMIT = int(os.getenv("MAX_RECURRSION_LIMIT", 50))
MAX_IO_PAIR = int(os.getenv("MAX_IO_PAIR", 10))


# special tokens
class PythonReportError(StrEnum):
    OPTIONAL_ARG_ABSENT = "<OPTIONAL_ARG_ABSENT>"
    RECURSION_LIMIT_EXCEEDED = "<RECURSION_LIMIT_EXCEEDED>"
    UNKNOWN_FILE = "<UNKNOWN_FILE>"
    UNABLE_TO_STRINGIFY = "<UNABLE_TO_STRINGIFY>"
    UNEXPECTED_CLASS_INSTANCE = "<UNEXPECTED_CLASS_INSTANCE>"
