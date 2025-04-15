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

    def _sumarNodos(self, nodo):
        if nodo is None:
            return 0
        return nodo.valor + self._sumarNodos(nodo.izquierda) + self._sumarNodos(nodo.derecha)
    
    def sumarNodos(self):
        return self._sumarNodos(self.raiz)


arbol = ArbolBinario()
n = int(input("Ingrese el número de nodos: "))

for i in range(n):
    x = int(input("Ingrese un valor para agregar: "))
    arbol.agregarValor(x)

print(arbol.sumarNodos())