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


class Node:
  '''Define el Nodo que utilizaremos en la linked list del inventario'''
  def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
  cProfile.runctx("__init__", globals(), locals())

class SLinkedList:
  '''Define la linked list que utilizaremos para manejar nuestro inventario'''
  def __init__(self):#, save
    self.headval = None
    # self.save = save

  def agregar(self, newdata):#, sqlthis = True
      '''Agrega un nuevo valor al nodo'''
      nodoNuevo = Node(newdata)
      if nodoNuevo is not None:
        nodoNuevo.nextval = self.headval
        self.headval = nodoNuevo
        # if self.save is True:
        #       if sqlthis is True:#para no insertar lo del query al inicializar el app
        #         cursor.execute("INSERT INTO Inventario (Producto, Precio, Inventario) VALUES (?, ?, ?)", nodoNuevo.dataval[0], nodoNuevo.dataval[1], nodoNuevo.dataval[2])

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
          # if(columna == 'Borrar'):
          #   cursor.execute("DELETE FROM Inventario WHERE Producto = '%s'" % (producto))
          # else:
          if(columna == 'Inventario'):
            newArr =[str(producto),float(nodo.dataval[1]),int(newval)]
            # cursor.execute("UPDATE Inventario SET Inventario = %s WHERE Producto = '%s'" % (newArr[2],newArr[0] ))
          elif(columna == 'Precio'):
            newArr =[str(producto),float(newval),int(nodo.dataval[2])]
            # cursor.execute("UPDATE Inventario SET Precio = %f WHERE Producto = '%s'" % (newArr[1],newArr[0] ))
          self.agregar(newArr) #, sqlthis= False
          break
        nodo = nodo.nextval
    return(productoList)

def mayus(palabra):
  ''' convierte a mayuscula la palabra o  string dada'''
  nvp = palabra.upper()
  return nvp

inventario = SLinkedList()
ordenesQueue = Queue(maxsize=6)
ordenes = HashTable(size = 50)
