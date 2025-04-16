class NodoCola:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        
class Cola:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def enqueue(self, valor):
        nodo = NodoCola(valor)
        if self.back is not None:
            self.back.next = nodo
        self.back = nodo
        self.size += 1
        if self.front is None:
            self.front = nodo
    
    def dequeue(self):
        nodo = self.front
        if nodo is not None:
            self.front = nodo.next
            self.size -= 1
            if self.front is None:
                self.back = None

    def peek(self):
        if self.front is not None:
            return self.front.valor
        return None
            
    def is_empty(self):
        return self.size == 0

    def print(self):
        nodo = self.front
        while nodo is not None:
            print(nodo.valor, end = (" -> " if nodo.next is not None else "\n"))
            nodo = nodo.next

    def clear(self):
        while not self.is_empty():
            self.dequeue()
