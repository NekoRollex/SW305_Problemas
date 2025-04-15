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
            self.pop()

class NodoArbolBinario:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

class ArbolBinario:
    def __init__(self):
        self.root = None
        self.size = 0

    def _add(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.left is None:
                nodo.left = NodoArbolBinario(valor)
            else:
                self._add(nodo.left, valor)
        else:
            if nodo.right is None:
                nodo.right = NodoArbolBinario(valor)
            else:
                self._add(nodo.right, valor)

    def add(self, valor):
        self.size += 1
        if self.root is None:
            self.root = NodoArbolBinario(valor)
        else:
            self._add(self.root, valor)

    def _print(self, nodo):
        if nodo is not None:
            self._print(nodo.left)
            print(nodo.valor, end=' -> ')
            self._print(nodo.right)

    def print(self):
        self._print(self.root)
        print(end = "\n")

    def empty(self):
        return self.size == 0

def bfs(arbol):
    if arbol.empty():
        return None
    
    cola = Cola()
    cola.enqueue(arbol.root)

    while not cola.is_empty():
        nodo = cola.peek()
        cola.dequeue()

        if nodo.left is not None:
            cola.enqueue(nodo.left)
        if nodo.right is not None:
            cola.enqueue(nodo.right)

        print(nodo.valor, end = " -> ")

arbol = ArbolBinario()

arbol.add(5)
arbol.add(3)
arbol.add(7)
arbol.add(2)
arbol.add(4)
arbol.add(6)
arbol.add(8)
arbol.add(1)

bfs(arbol)
