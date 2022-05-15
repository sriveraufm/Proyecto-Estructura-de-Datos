from __future__ import print_function

import bisect
import timeit


def binarysearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


def bisect_index(alist, item):
    idx = bisect.bisect_left(alist, item)
    if idx != len(alist) and alist[idx] == item:
        found = True
    else:
        found = False
    return found


time_tests = [
    ("    'LECHE' in ['CAFE', 'LECHE', 'PAN', 'CHOCOLATE', 'AGUA']",
     "'LECHE' in alist",
     "alist = ['CAFE', 'LECHE', 'PAN', 'CHOCOLATE', 'AGUA']"),

    ("    'LECHE' in ['CAFE', 'LECHE', 'PAN', 'CHOCOLATE', 'AGUA', 'PASTEL', 'DESODORANTE', 'SERVILLETAS']",
     "'LECHE' in alist",
     "alist = ['CAFE', 'LECHE', 'PAN', 'CHOCOLATE', 'AGUA', 'PASTEL', 'DESODORANTE', 'SERVILLETAS']"),



    ("    'LECHE' in set(['CAFE', 'LECHE', 'PAN', 'CHOCOLATE', 'AGUA'])",
     "'LECHE' in aset",
     "aset = set(['CAFE', 'LECHE', 'PAN', 'CHOCOLATE', 'AGUA'])"),

    ("'LECHE' in set(['CAFE', 'LECHE', 'PAN', 'CHOCOLATE', 'AGUA', 'PASTEL', 'DESODORANTE', 'SERVILLETAS'])",
     "'LECHE' in aset",
     "aset = set(['CAFE', 'LECHE', 'PAN', 'CHOCOLATE', 'AGUA', 'PASTEL', 'DESODORANTE', 'SERVILLETAS'])"),



    ("binarysearch(['CAFE', 'LECHE', 'PAN', 'CHOCOLATE', 'AGUA'], 'LECHE')",
     "binarysearch(alist, 'LECHE')",
     "from __main__ import binarysearch; alist = ['CAFE', 'LECHE', 'PAN', 'CHOCOLATE', 'AGUA']"),

    ("binarysearch(['CAFE', 'LECHE', 'PAN', 'CHOCOLATE', 'AGUA', 'PASTEL', 'DESODORANTE', 'SERVILLETAS'], 'LECHE')",
     "binarysearch(alist, 'LECHE')",
     "from __main__ import binarysearch; alist = ['CAFE', 'LECHE', 'PAN', 'CHOCOLATE', 'AGUA', 'PASTEL', 'DESODORANTE', 'SERVILLETAS']"),



    ("bisect_index(['CAFE', 'LECHE', 'PAN', 'CHOCOLATE', 'AGUA'], 'LECHE')",
     "bisect_index(alist, 'LECHE')",
     "from __main__ import bisect_index; alist = ['CAFE', 'LECHE', 'PAN', 'CHOCOLATE', 'AGUA']"),

    ("bisect_index(['CAFE', 'LECHE', 'PAN', 'CHOCOLATE', 'AGUA', 'PASTEL', 'DESODORANTE', 'SERVILLETAS'], 'LECHE')",
     "bisect_index(alist, 'LECHE')",
     "from __main__ import bisect_index; alist = ['CAFE', 'LECHE', 'PAN', 'CHOCOLATE', 'AGUA', 'PASTEL', 'DESODORANTE', 'SERVILLETAS']"),
    ]

for display, statement, setup in time_tests:
    result = timeit.timeit(statement, setup, number=1000000)
    print("{0:<45}{1}".format(display, result))


print('LECHE' in set(['LECHE', 'CAFE']))