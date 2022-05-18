class Node:
    '''Define el Nodo que utilizaremos en la linked list del inventario'''
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    '''Define la linked list que utilizaremos para manejar nuestro inventario'''
    def __init__(self):
        self.headval = None
    def agregar(self, newdata):
        '''Agrega un nuevo valor al nodo'''
        nodoNuevo = Node(newdata)
        if nodoNuevo is not None:
            nodoNuevo.nextval = self.headval
            self.headval = nodoNuevo
    def listprint(self):
        ''' imprime todos los nodos de la lista'''
        nodo = self.headval
        while nodo is not None:
            print (nodo.dataval,end="->")
            nodo = nodo.nextval
    def listfind(self, producto):
        '''busca el nodo que contenga el producto dado'''
        nodo = self.headval
        productoList = None
        while nodo is not None:
            if(nodo.dataval[0] == producto):
                productoList = nodo.dataval
            nodo = nodo.nextval
        return(productoList)

# test = LinkedList()
# test.agregar('test')
# test.agregar('test2')
# test.listprint()
