
class NodoPila:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        
class Pila:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, valor):
        nodo = NodoPila(valor)
        nodo.next = self.top
        self.top = nodo
        self.size += 1
    
    def pop(self):
        nodo = self.top
        if not self.is_empty():
            self.top = nodo.next
            self.size -= 1

    def peek(self):
        if self.top is not None:
            return self.top.valor
        return None
            
    def is_empty(self):
        return self.size == 0

    def print(self):
        nodo = self.top
        while nodo is not None:
            print(nodo.valor, end = (" -> " if nodo.next is not None else "\n"))
            nodo = nodo.next
