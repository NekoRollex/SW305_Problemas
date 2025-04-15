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


    def _inOrden(self, nodo):
        if nodo is not None:
            self._inOrden(nodo.izquierda)
            print(nodo.valor, end=' -> ')
            self._inOrden(nodo.derecha)

    def inOrden(self):
        self._inOrden(self.raiz)
        print(end="\n")