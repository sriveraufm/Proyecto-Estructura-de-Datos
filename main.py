from pickle import FALSE, TRUE
import csv
from sys import maxsize
import uuid
import os.path
import json
import cProfile
from flask import jsonify
from hashtable import HashTable
from Queue import Queue
from grafo import *
from LinkedList import * 
from BPlusTreeV2 import BPlusTree
def mayus(palabra):
  ''' convierte a mayuscula la palabra o  string dada'''
  nvp = palabra.upper()
  return nvp

inventario = HashTable(size=50)
ordenesQueue = Queue(maxsize=6)
ordenes = HashTable(size = 50)

# cada key es una zona de la ciudad
ciudad = {
    0 : [10, 15],#CARRETERA
    1 : [3, 5, 2, 6],
    2 : [1, 7, 6],
    3 : [7, 1, 8],
    4 : [1, 3, 8, 9, 5],
    5 : [1, 8, 10],
    6 : [1, 17],
    7 : [19, 11],
    8 : [11, 3, 9, 10],
    9 : [13, 11, 8, 10,4],
    10 : [0, 15, 14, 9, 5],
    11 : [12, 13, 7],
    12 : [11, 8, 13, 21],
    13 : [12, 14, 9],
    14 : [13, 10],
    15 : [0, 10, 16, 5],
    16 : [15, 17],
    17 : [6, 18],
    18 : [17],
    19 : [7],
    # 20 : [],
    21 : [12]
}

cadena = ciudadGT(ciudad)

registroDespacho = LinkedList()

clientesTree = BPlusTree()