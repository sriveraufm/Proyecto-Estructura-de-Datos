from __future__ import print_function

import bisect
import timeit

from hashtable import *

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


hashtest = HashTable(50)
hashtest.set_val('CAFE',0)
hashtest.set_val('LECHE',0)
hashtest.set_val('PAN',0)
hashtest.set_val('CHOCOLATE',0)
hashtest.set_val('AGUA',0)

hashtest2 = HashTable(50)
hashtest2.set_val('CAFE',0)
hashtest2.set_val('LECHE',0)
hashtest2.set_val('PAN',0)
hashtest2.set_val('CHOCOLATE',0)
hashtest2.set_val('AGUA',0)
hashtest2.set_val('PASTEL',0)
hashtest2.set_val('DESODORANTE',0)
hashtest2.set_val('SERVILLETAS',0)

import time

t0 = time.time()

hashtest.exists('LECHE')

t1 = time.time()

test = float(t1-t0)

print("size pequeno... hashtest.exists('LECHE') TIME: ", format(test, '.16f'))

t0 = time.time()

hashtest2.exists('LECHE')

t1 = time.time()
print("siez grande... hashtest2.exists('LECHE') TIME: ", format(t1-t0, '.16f'))


hashtest3 = HashTable(50)
hashtest3.set_val('CAFE',0)
hashtest3.set_val('LECHE',0)
hashtest3.set_val('PAN',0)
hashtest3.set_val('CHOCOLATE',0)
hashtest3.set_val('AGUA',0)
hashtest3.set_val('PASTEL',0)
hashtest3.set_val('DESODORANTE',0)
hashtest3.set_val('SERVILLETAS',0)
hashtest3.set_val('CAF3E',0)
hashtest3.set_val('LECHdE',0)
hashtest3.set_val('PAN1d',0)
hashtest3.set_val('CHOCd1wOLATE',0)
hashtest3.set_val('AGUdw1A',0)
hashtest3.set_val('PASTEd1L',0)
hashtest3.set_val('DESODORd1ANTE',0)
hashtest3.set_val('SERVILLEd1wTAS',0)

hashtest3.set_val('CAd1dwFE',0)
hashtest3.set_val('LECHdw1E',0)
hashtest3.set_val('PAd1wwN',0)
hashtest3.set_val('CHOCOLw1123ATE',0)
hashtest3.set_val('AGU1441A',0)
hashtest3.set_val('PASTEf1f1fL',0)
hashtest3.set_val('DESODORff1f1f1ANTE',0)
hashtest3.set_val('SERVILLETAf1ff11fS',3)


t0 = time.time()

hashtest3.exists('CAd1dwFE')

t1 = time.time()
print("sizE AUN MAS grande!... hashtest3.exists('LECHE') TIME: ", format(t1-t0, '.16f'))


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

