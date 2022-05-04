from pickle import FALSE, TRUE
import csv
from sys import maxsize
import uuid
import os.path
import json
import cProfile
import BPlusTreeV2

from flask import jsonify

# ordenes csv


"""Simple implementation of a B+ tree, a self-balancing tree data structure that (1) maintains sort
data order and (2) allows insertions and access in logarithmic time.
"""

class Node(object):
    """Base node object.
    Each node stores keys and values. Keys are not unique to each value, and as such values are
    stored as a list under each key.
    Attributes:
        order (int): The maximum number of keys each node can hold.
    """
    def __init__(self, order):
        """Child nodes can be converted into parent nodes by setting self.leaf = False. Parent nodes
        simply act as a medium to traverse the tree."""
        self.order = order
        self.keys = []
        self.values = []
        self.leaf = True

    def add(self, key, value):
        """Adds a key-value pair to the node."""
        # If the node is empty, simply insert the key-value pair.
        if not self.keys:
            self.keys.append(key)
            self.values.append([value])
            return None

        for i, item in enumerate(self.keys):
            # If new key matches existing key, add to list of values.
            if key == item:
                self.values[i].append(value)
                break

            # If new key is smaller than existing key, insert new key to the left of existing key.
            elif key < item:
                self.keys = self.keys[:i] + [key] + self.keys[i:]
                self.values = self.values[:i] + [[value]] + self.values[i:]
                break

            # If new key is larger than all existing keys, insert new key to the right of all
            # existing keys.
            elif i + 1 == len(self.keys):
                self.keys.append(key)
                self.values.append([value])

    def split(self):
        """Splits the node into two and stores them as child nodes."""
        left = Node(self.order)
        right = Node(self.order)
        mid = self.order // 2

        left.keys = self.keys[:mid]
        left.values = self.values[:mid]

        right.keys = self.keys[mid:]
        right.values = self.values[mid:]

        # When the node is split, set the parent key to the left-most key of the right child node.
        self.keys = [right.keys[0]]
        self.values = [left, right]
        self.leaf = False

    def is_full(self):
        """Returns True if the node is full."""
        return len(self.keys) == self.order

    def show(self, counter=0):
        """Prints the keys at each level."""
        print(counter, str(self.keys))

        # Recursively print the key of child nodes (if these exist).
        if not self.leaf:
            for item in self.values:
                item.show(counter + 1)

class BPlusTree(object):
    """B+ tree object, consisting of nodes.
    Nodes will automatically be split into two once it is full. When a split occurs, a key will
    'float' upwards and be inserted into the parent node to act as a pivot.
    Attributes:
        order (int): The maximum number of keys each node can hold.
    """
    def __init__(self, order=8):
        self.root = Node(order)

    def _find(self, node, key):
        """ For a given node and key, returns the index where the key should be inserted and the
        list of values at that index."""
        for i, item in enumerate(node.keys):
            if key < item:
                return node.values[i], i

        return node.values[i + 1], i + 1

    def _merge(self, parent, child, index):
        """For a parent and child node, extract a pivot from the child to be inserted into the keys
        of the parent. Insert the values from the child into the values of the parent.
        """
        parent.values.pop(index)
        pivot = child.keys[0]

        for i, item in enumerate(parent.keys):
            if pivot < item:
                parent.keys = parent.keys[:i] + [pivot] + parent.keys[i:]
                parent.values = parent.values[:i] + child.values + parent.values[i:]
                break

            elif i + 1 == len(parent.keys):
                parent.keys += [pivot]
                parent.values += child.values
                break

    def insert(self, key, value):
        """Inserts a key-value pair after traversing to a leaf node. If the leaf node is full, split
        the leaf node into two.
        """
        parent = None
        child = self.root

        # Traverse tree until leaf node is reached.
        while not child.leaf:
            parent = child
            child, index = self._find(child, key)

        child.add(key, value)

        # If the leaf node is full, split the leaf node into two.
        if child.is_full():
            child.split()

            # Once a leaf node is split, it consists of a internal node and two leaf nodes. These
            # need to be re-inserted back into the tree.
            if parent and not parent.is_full():
                self._merge(parent, child, index)

    def retrieve(self, key):
        """Returns a value for a given key, and None if the key does not exist."""
        child = self.root

        while not child.leaf:
            child, index = self._find(child, key)

        for i, item in enumerate(child.keys):
            if key == item:
                return child.values[i]
        return None

    def show(self):
        """Prints the keys at each level."""
        self.root.show()


bplustree = BPlusTree(order=4)

class Queue:
    #inicializacion
    def __init__(self, maxsize):
        self.queue = []
    #agregar un valor al queue
    def add(self, valor):
        if(self.size() < maxsize):
          self.queue.append(valor)

    def get(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def top(self):
          return self.queue[0]

    def full(self):
        return len(self.queue) == maxsize

    def empty(self):
        return len(self.queue) == 0


ordenesQueue = Queue(maxsize=6)

col = 5
row = 0
ordenes = [[0] * col for i in range(row)]
if os.path.isfile('ordenes.csv'):
  with open('ordenes.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for rows in csv_reader:
            if(any(rows)):
              ordenes.append([j for j in rows])
else:
    ordenes.append([j for j in ['ID',"NOMBRE","CANTIDAD","ESTADO","TOTAL"]])
    with open("ordenes.csv", "w") as f:
      writer = csv.writer(f)
      writer.writerows(ordenes)
      
class Node:
  '''Define el Nodo que utilizaremos en la linked list del inventario'''
  def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
  cProfile.runctx("__init__", globals(), locals())



class SLinkedList:
  '''Define la linked list que utilizaremos para manejar nuestro inventario'''
  def __init__(self):
    self.headval = None
  def agregar(self, newdata,save = None):
      '''Agrega un nuevo valor al nodo'''
      nodoNuevo = Node(newdata)
      if self.headval is None:
        self.headval = nodoNuevo
        return
      nodo = self.headval
      while(nodo.nextval is not None):
        nodo = nodo.nextval
      nodo.nextval=nodoNuevo
      if save is None:
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


def eliminar(nbr):
    '''Elimina la orden dado el id'''
    si = 0
    for i in range(0,len(ordenes)):
        if(i > 0):
          if str(ordenes[i][0])== nbr:
              si = 1
              arr2 = ordenes[0:i][0:col] + ordenes[i + 1:len(ordenes)][0:col]#
    if(si == 0):
      arr2 = ordenes  
    return(arr2)

def guardar():
  '''Guarda el array multidimensional de ordenes en un archivo csv para conservar los cambios'''
  with open("ordenes.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(ordenes)


inventario = SLinkedList()
# # inventario csv
if os.path.isfile('inventario.csv'):
  with open('inventario.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for rows in csv_reader:
          if(any(rows)):
            # print([j for j in rows])
            inventario.agregar([j for j in rows],0)
            bplustree.insert(str(rows[0]), str(rows[0]))
  # inventario.headval.nextval = None
else:
  inventario.headval = Node(["Producto","Precio","Inventario"])# columnas
  nodo = inventario.headval
  with open("inventario.csv", "w") as f:
      # print(header.dataval)
      writer = csv.writer(f)
      writer.writerows([nodo.dataval])


def printOrdenes():
    '''Imprime el array multidimensional de ordenes'''
    for r in ordenes:
      print( ' '.join([str(x) for x in r] ) ) 
      


