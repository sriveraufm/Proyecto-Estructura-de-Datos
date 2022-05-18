from LinkedList import LinkedList
import time
import json
from flask import jsonify
testllist = LinkedList()
import sys, os
# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__
t0 = time.time()
for i in range(5000):
    testllist.agregar(i)

t1 = time.time()
print("El linked list se tardó en agregar los items: ", format(t1-t0, '.16f'))

blockPrint()


t0 = time.time()
testllist.listprint()

t1 = time.time()
enablePrint()
print("El linked list se tardó en regresar lo items como lista visualizable: ", format(t1-t0, '.16f'))

testlist = []
t0 = time.time()
for i in range(5000):
    testlist.append(i)

t1 = time.time()

print("La lista se tardó en agregar los items: ", format(t1-t0, '.16f'))

