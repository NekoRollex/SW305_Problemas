class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
class ListaEnlazada:
    def __init__(self):
        self.inicio = None
        self.final = None

    def insertar(self, valor):
        nodo = Nodo(valor)
        if self.final is not None:
            self.final.siguiente = nodo
        self.final = nodo
        if self.inicio is None:
            self.inicio = nodo
            
    def print(self):
        nodo = self.inicio
        print("Lista enlazada:", end=" ")
        while nodo is not None:
            print(nodo.valor, end=(" -> " if nodo.siguiente is not None else "\n"))
            nodo = nodo.siguiente



