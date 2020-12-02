#!/usr/bin/env python

import timeit

setup_code = """"""

codes = [
    '''''',
    '''''',
]

for code in codes:
    t = timeit.Timer(code, setup_code)
    print(code, '\n')
    print(t.timeit(10000))
    print()
