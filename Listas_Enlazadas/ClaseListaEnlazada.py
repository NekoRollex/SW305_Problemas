class NodoLista:
    def __init__(self, valor):
        self.valor = valor
        self.right = None
        self.left = None

class ListaEnlazada:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def push_back(self, valor):
        nuevo_nodo = NodoLista(valor)
        if self.size == 0:
            self.front = nuevo_nodo
            self.back = nuevo_nodo
        else:
            self.back.right = nuevo_nodo
            nuevo_nodo.left = self.back
            self.back = nuevo_nodo
        self.size += 1

    def push_front(self, valor):
        nuevo_nodo = NodoLista(valor)
        if self.size == 0:
            self.front = nuevo_nodo
            self.back = nuevo_nodo
        else:
            nuevo_nodo.right = self.front
            self.front.left = nuevo_nodo
            self.front = nuevo_nodo
        self.size += 1

    def print(self):
        nodo = self.front
        while nodo is not None:
            print(nodo.valor, end = " -> ")
            nodo = nodo.right
        print(end = "\n");