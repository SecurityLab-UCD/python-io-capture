import os


MAX_REPORT_SIZE = int(os.getenv("MAX_REPORT_SIZE", 10))
DUMP_FILE_NAME = os.getenv("DUMP_FILE_NAME", "py_io_capture_report.json")
MAX_RECURRSION_LIMIT = int(os.getenv("MAX_RECURRSION_LIMIT", 20))
