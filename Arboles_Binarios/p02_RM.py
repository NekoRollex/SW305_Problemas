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

    def _inOrden(self, nodo):
        if nodo is not None:
            self._inOrden(nodo.izquierda)
            print(nodo.valor, end=' -> ')
            self._inOrden(nodo.derecha)

    def inOrden(self):
        self._inOrden(self.raiz)
        print(end="\n")

arbol = ArbolBinario()

arbol.agregarValor(5)
arbol.agregarValor(3)
arbol.agregarValor(7)
arbol.agregarValor(2)
arbol.agregarValor(4)
arbol.agregarValor(6)
arbol.agregarValor(8)

arbol.inOrden()