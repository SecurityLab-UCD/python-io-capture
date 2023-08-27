from example import example
import sys
import numpy as np

###### lines to be added to fuzz_* scripts ###########
from src.io_capture import decorate_module, dump_records
import atexit

example = decorate_module(example)
np = decorate_module(np)

# todo: get dump file path from env variable
atexit.register(dump_records, "demo_dump.json")
######################################################

if __name__ == "__main__":
    # example projects
    example.main()
    example.main()

    # real world projects
    xs = [1, 2, 3, 4, 5]
    np.mean(xs)
    np.sort(xs)
