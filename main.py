from pickle import FALSE, TRUE
import csv
from sys import maxsize
import uuid
import os.path
import json
import cProfile
from flask import jsonify
import pyodbc 



conn = pyodbc.connect
                    'Driver={SQL Server};'
                    'Server=estructurasufm.mssql.somee.com;'
                    'Database=estructurasufm;'
                    'UID=srivera_SQLLogin_1;'
                    'PWD=ec2wfr9qzh;'
                    'Trusted_Connection=no;'
                    )
conn.autocommit = True
cursor = conn.cursor()

class Node:
  '''Clase de nodo para el stack'''
  def __init__(self, value = None):
    self.dataval = value
    self.nextval = None

class Stack:
    '''Inicializacion del stack'''
    def __init__(self):
        self.headval = Node()
    ''' funcion para regresar el stack como una lista'''
    def get(self):
        nodo = self.headval
        stackArr = []
        while nodo:
            stackArr.append(str(nodo.dataval))
            nodo = nodo.nextval
        return stackArr
    '''Funcion para agregar un valor dado hasta arriba del stack'''
    def add(self, dataval):
        node = Node(dataval)
        node.nextval = self.headval
        self.headval = node


registro = Stack()

class Queue:
    '''Define nuestro queue'''
    '''inicializacion'''
    def __init__(self, maxsize):
        self.queue = []
        self.maxsize = maxsize
    '''agregar un valor al queue'''
    def add(self, valor):
        if(self.size() < self.maxsize):
          self.queue.append(valor)
    '''imprime y quita el primer elemento del queue'''
    def get(self):
        if(self.size() > 0):
          return self.queue.pop(0)
        else:
            return None
    '''regresa el tamaño del queue'''
    def size(self):
        return len(self.queue)
    '''imprime el primer elemento del queue sin borrarlo'''
    def top(self):
          return self.queue[0]
    '''regresa si el queue esta lleno o no'''
    def full(self):
        return self.size() == self.maxsize
    '''regresa si el queue esta vacio o no'''
    def empty(self):
        return len(self.queue) == 0
    def anular(self, id):
        if(self.size() > 0):
            for i in range(self.size()-1):
                  if self.queue[i] == id:
                      self.queue.pop(i)
        else:
            return None

ordenesQueue = Queue(maxsize=6)

class HashTable:
    
	# Create empty bucket list of given size
    def __init__(self, size, save):
        self.size = size
        self.hash_table = self.create_buckets()
        self.keys = []
        self.save = save

    def create_buckets(self):
        return [[] for _ in range(self.size)]

	# Insert values into hash map
    def set_val(self, key, val, sqlthis = True):
		
		# Get the index from the key
		# using hash function
        hashed_key = hash(key) % self.size
		
		# Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index in range(len(bucket)):
            record = bucket[index]
            record_key, record_val = record
			
			# check if the bucket has same key as
			# the key to be inserted
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
            cursor.execute("UPDATE Ordenes SET ESTADO = '%s' WHERE ID = '%s'" % ("PAGADA",key))
        else:
            self.keys.append(key)
            bucket.append((key, val))
            if sqlthis:
              cursor.execute("INSERT INTO Ordenes (ID, NOMBRE, CANTIDAD, ESTADO, TOTAL) VALUES (?, ?, ?, ?, ?)", str(key), str(val[0]), str(val[1]), str(val[2]), str(val[3]))


    # Return searched value with specific key
    def get_val(self, key):

    # Get the index from the key using
    # hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index in range(len(bucket)):
            record = bucket[index]
            record_key, record_val = record

            # check if the bucket has same key as
            # the key being searched
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"

    # Remove a value with specific key
    def delete_val(self, key):
    # Get the index from the key using
    # hash function
        hashed_key = hash(key) % self.size
    # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index in range(len(bucket)):
            record = bucket[index]
            record_key, record_val = record
            # check if the bucket has same key as
            # the key to be deleted
            if str(record_key) == str(key):
                found_key = True
                break
        if found_key is True:
            cursor.execute("DELETE FROM Ordenes WHERE ID = '%s'" % (key))
            bucket.pop(index)
        return (found_key)
            
    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

class Node:
  '''Define el Nodo que utilizaremos en la linked list del inventario'''
  def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
  cProfile.runctx("__init__", globals(), locals())

class SLinkedList:
  '''Define la linked list que utilizaremos para manejar nuestro inventario'''
  def __init__(self, save):
    self.headval = None
    self.save = save

  def agregar(self, newdata, sqlthis = True):
      '''Agrega un nuevo valor al nodo'''
      nodoNuevo = Node(newdata)
      if nodoNuevo is not None:
        nodoNuevo.nextval = self.headval
        self.headval = nodoNuevo
        if self.save is True:
              if sqlthis is True:
                cursor.execute("INSERT INTO Inventario (Producto, Precio, Inventario) VALUES (?, ?, ?)", nodoNuevo.dataval[0], nodoNuevo.dataval[1], nodoNuevo.dataval[2])

  def borrar(self, nrow):
    '''Elimina el nodo de la linked list en la posicion dada'''
    if self.headval is None:
        return(0)
    nodo = self.headval
    if nrow == 0:
        self.headval = nodo.nextval
        nodo = None
        return(0)
    for i in range(nrow - 1):
        nodo = nodo.nextval
        if nodo is None:
            break
    if nodo is None:
        return(0)
    if nodo.nextval is None:
        return(0)
    next = nodo.nextval.nextval
    nodo.nextval = None
    nodo.nextval = next
    # self.exportarcsv()#guarda cambios a csv
    
  def rows(self):
      ''' funcion simple para calcular el largo de la lista'''
      nodo = self.headval
      rowCount = 0
      while (nodo is not None):
          rowCount += 1
          nodo = nodo.nextval
      return rowCount
  def listprint(self):
    ''' imprime todos los nodos de la lista'''
    nodo = self.headval
    while nodo is not None:
      print (nodo.dataval)
      nodo = nodo.nextval
  def listfind(self, producto):
    '''busca el nodo que contenga el producto dado'''
    nodo = self.headval
    productoList = None
    while nodo is not None:
      # print(nodo.dataval)
      if(nodo.dataval[0] == producto):
        productoList = nodo.dataval
      nodo = nodo.nextval
    return(productoList)
  def getNode(self, indice):
    '''imprime el nodo dado el indice de la lista'''
    nodo = self.headval
    for i in range(int(indice)):
      nodo = nodo.nextval
    print(nodo.dataval)  
    
  def listmodify(self,producto,newval, columna):
    '''Funcion para modificar un nuevo valor de cualquier "columna" que le digmaos del nodo'''
    nodo = self.headval
    productoList = None
    nrow = self.rows()
    if(int(nrow) is not None):
      for i in range(int(nrow)): 
        if(nodo.dataval[0] == producto):
          self.borrar(i)
          if(columna == 'Borrar'):
            cursor.execute("DELETE FROM Inventario WHERE Producto = '%s'" % (producto))
          else:
            if(columna == 'Inventario'):
              newArr =[str(producto),float(nodo.dataval[1]),int(newval)]
              cursor.execute("UPDATE Inventario SET Inventario = %s WHERE Producto = '%s'" % (newArr[2],newArr[0] ))
            elif(columna == 'Precio'):
              newArr =[str(producto),float(newval),int(nodo.dataval[2])]
              cursor.execute("UPDATE Inventario SET Precio = %f WHERE Producto = '%s'" % (newArr[1],newArr[0] ))
            self.agregar(newArr, sqlthis= False) 
            break
        nodo = nodo.nextval
    return(productoList)
    



def mayus(palabra):
  ''' convierte a mayuscula la palabra o  string dada'''
  nvp = palabra.upper()
  return nvp


def guardar():
  '''Guarda las ordenes en un archivo csv para conservar los cambios'''
  
  with open('ordenes.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['ID','NOMBRE','CANTIDAD','ESTADO','TOTAL'])
    writer.writeheader()
    for key in ordenes.keys:
        item = ordenes.get_val(key)
        item.update({'ID': key})
        writer.writerow(item)


inventario = SLinkedList(save = True)

inventarioDB = list(cursor.execute('SELECT TRIM(Producto), Precio, Inventario FROM Inventario'))

for row in inventarioDB:## no se de que otra forma hacerlo, esta no es la mejor forma!
      inventario.agregar(row, sqlthis= False)
inventario.listprint()

ordenes = HashTable(size = 50, save = True)
ordenesDB = list(cursor.execute('SELECT TRIM(ID), TRIM(NOMBRE),CANTIDAD, TRIM(ESTADO), TOTAL FROM Ordenes'))

from itertools import chain
for row in ordenesDB:## no se de que otra forma hacerlo, esta no es la mejor forma!
  ordenes.set_val(row[0], row[1:5], sqlthis= False)
