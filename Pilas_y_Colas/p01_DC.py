class NodoPila:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        
class Pila:
    def __init__(self):
        self.top = None

    def push(self, valor):
        nodo = NodoPila(valor)
        nodo.next = self.top
        self.top = nodo
    
    def pop(self):
        if not self.is_empty():
            nodo = self.top
            self.top = nodo.next

    def peek(self):
        if self.top is not None:
            return self.top.valor
        return None
            
    def is_empty(self):
        return self.top is None
