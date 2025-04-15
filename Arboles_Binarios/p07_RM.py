class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def _agregarValor(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._agregarValor(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._agregarValor(nodo.derecha, valor)

    def agregarValor(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregarValor(self.raiz, valor)


    def _contarNodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contarNodos(nodo.izquierda) + self._contarNodos(nodo.derecha)

    def contarNodos(self):
        return self._contarNodos(self.raiz)

arbol = ArbolBinario()    
n = int(input("Ingrese el número de nodos: "))

for i in range(n):
    x = int(input("Ingrese un valor para agregar: "))
    arbol.agregarValor(x)

print("Cantidad de nodos:", arbol.contarNodos())