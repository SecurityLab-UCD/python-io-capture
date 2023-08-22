from example import example
import sys
import numpy as np

###### lines to be added to fuzz_* scripts ###########
from src.report import instrument_report

instrument_report(example)
instrument_report(np)
######################################################

if __name__ == "__main__":
    # example projects
    example.main()

    # real world projects
    xs = [1, 2, 3, 4, 5]
    np.mean(xs)
    np.pad(xs, (2, 3), "constant")
