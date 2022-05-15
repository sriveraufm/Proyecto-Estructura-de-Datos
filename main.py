from pickle import FALSE, TRUE
import csv
from sys import maxsize
import uuid
import os.path
import json
import cProfile
from flask import jsonify
from hashtable import HashTable

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
        nodo = self.headval.nextval
        stackArr = []
        while nodo:
            stackArr.append(str(nodo.dataval))
            nodo = nodo.nextval
        return stackArr
    '''Funcion para agregar un valor dado hasta arriba del stack'''
    def add(self, dataval):
        node = Node(dataval)
        node.nextval = self.headval.nextval
        self.headval.nextval = node


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

ordenes = HashTable(size = 50)
ordenesQueue = Queue(maxsize=6)

col = 5
row = 0
# ordenes = [[0] * col for i in range(row)]
# if os.path.isfile('ordenes.csv'):
#   with open('ordenes.csv') as csv_file:
#       csv_reader = csv.reader(csv_file, delimiter=',')
#       line_count = 0
#       for rows in csv_reader:
#             if(any(rows)):
#               ordenes.append([j for j in rows])
# else:
#     ordenes.append([j for j in ['ID',"NOMBRE","CANTIDAD","ESTADO","TOTAL"]])
#     with open("ordenes.csv", "w") as f:
#       writer = csv.writer(f)
#       writer.writerows(ordenes)


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
  def agregar(self, newdata,save = True):
      '''Agrega un nuevo valor al nodo'''
      nodoNuevo = Node(newdata)
      if self.headval is None:
        self.headval = nodoNuevo
        return
      nodo = self.headval
      while(nodo.nextval is not None):
        nodo = nodo.nextval
      nodo.nextval=nodoNuevo
      if self.save is True:
        self.exportarcsv()#guarda cambios a csv

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
    self.exportarcsv()#guarda cambios a csv
    
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
    nodo = self.headval.nextval
    productoList = None
    while nodo is not None:
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
    nodo = self.headval.nextval
    productoList = None
    nrow = self.rows()
    if(int(nrow) is not None):
      for i in range(int(nrow)): 
        if(nodo.dataval[0] == producto):
          self.borrar(i+1)
          if(columna == 'Inventario'):
            newArr =[str(producto),float(nodo.dataval[1]),int(newval)]
          elif(columna == 'Precio'):
            newArr =[str(producto),float(newval),int(nodo.dataval[2])]
          elif(columna == 'Producto'):
            newArr =[str(newval),float(nodo.dataval[1]),int(nodo.dataval[2])]
          self.agregar(newArr)
          break
        nodo = nodo.nextval
    return(productoList)
    
  def exportarcsv(self):
    '''Exporta la lista a un archivo csv para poder guardar los cambios'''
    nodo = self.headval
    with open("inventario.csv", "w") as f:
      while nodo is not None:
        writer = csv.writer(f)
        writer.writerows([nodo.dataval])
        nodo = nodo.nextval


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
# # inventario csv
if os.path.isfile('inventario.csv'):
  with open('inventario.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for rows in csv_reader:
          if(any(rows)):
            # print([j for j in rows])
            inventario.agregar([j for j in rows],0)
  # inventario.headval.nextval = None
else:
  inventario.headval = Node(["Producto","Precio","Inventario"])# columnas
  nodo = inventario.headval
  with open("inventario.csv", "w") as f:
      # print(header.dataval)
      writer = csv.writer(f)
      writer.writerows([nodo.dataval])


# def printOrdenes():
#     '''Imprime el array multidimensional de ordenes'''
#     for r in ordenes:
#       print( ' '.join([str(x) for x in r] ) ) 
      


