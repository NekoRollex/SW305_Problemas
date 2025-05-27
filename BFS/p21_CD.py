# 21. Encontrar el nodo más lejano desde la raíz, en un árbol, encontrar el nodo que se encuentra a mayor
#     profundidad desde la raíz.

class NodoCola:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
class Cola:
    def __init__(self):
        self.inicio = None
        self.final = None

    def enqueue(self, valor):
        nodo = NodoCola(valor)
        if self.final is not None:
            self.final.siguiente = nodo
        self.final = nodo
        if self.inicio is None:
            self.inicio = nodo
    
    def dequeue(self):
        nodo = self.inicio
        if nodo is not None:
            self.inicio = nodo.siguiente
            if self.inicio is None:
                self.final = None
            return nodo.valor
        return None


    def peek(self):
        if self.inicio is not None:
            return self.inicio.valor
        return None
            
    def is_empty(self):
        return self.inicio is None


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def _agregarValor(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierda = self._agregarValor(nodo.izquierda, valor)
        else:
            nodo.derecha = self._agregarValor(nodo.derecha, valor)
        return nodo

    def agregarValor(self, valor):
        self.raiz = self._agregarValor(self.raiz, valor)

def BFS(arbol):
    if arbol.raiz is None:
        return None, []

    cola = Cola()
    cola.enqueue(arbol.raiz)
    mas_profundo = arbol.raiz
    recorrido = []

    while not cola.is_empty():
        actual = cola.dequeue()
        recorrido.append(actual.valor)
        mas_profundo = actual

        if actual.izquierda:
            cola.enqueue(actual.izquierda)
        if actual.derecha:
            cola.enqueue(actual.derecha)

    return mas_profundo, recorrido

def imprimir_arbol(nodo, nivel=0):
    if nodo is not None:
        imprimir_arbol(nodo.derecha, nivel + 1)
        print(' ' * 4 * nivel + '->', nodo.valor)
        imprimir_arbol(nodo.izquierda, nivel + 1)


arbol = ArbolBinario()
for valor in [10, 5, 15, 3, 7, 12, 20, 1, 8]:
    arbol.agregarValor(valor)

nodo_final, recorrido = BFS(arbol)

imprimir_arbol(arbol.raiz)

print("Recorrido BFS:", recorrido)
print("Nodo más profundo:", nodo_final.valor)