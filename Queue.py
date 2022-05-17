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
