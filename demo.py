from example import example
import sys
from charset_normalizer import from_bytes
from et_xmlfile import xmlfile
from io import BytesIO
from docutils import parsers, frontend, utils, ApplicationError

###### lines to be added to fuzz_* scripts ###########
from py_io_capture import decorate_module, dump_records, DUMP_FILE_NAME
from py_io_capture.io_capture import record_calls
import atexit

from_bytes = decorate_module(from_bytes)
xmlfile = decorate_module(xmlfile)
parsers = decorate_module(parsers)
utils = decorate_module(utils)
frontend = decorate_module(frontend)

atexit.register(dump_records, DUMP_FILE_NAME)
######################################################

if __name__ == "__main__":
    from_bytes(b"\\x01\\x00\\xff\\x9b")
    f2 = BytesIO()
    with xmlfile(f2) as xf:
        pass
    rst_parser_class = parsers.get_parser_class('rst')
    parser = rst_parser_class()
    document = utils.new_document(
        "abcdefg",
        frontend.get_default_settings(parser)
    )
    try:
        parser.parse("abcdefg", document)
    except ApplicationError:
        pass
    
