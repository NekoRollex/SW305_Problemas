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

    def _contarHojas(self, nodo):
        if nodo is None:
            return 0
        Iz = self._contarHojas(nodo.izquierda)
        De = self._contarHojas(nodo.derecha)
        return Iz + De + (1 if nodo.izquierda is None and nodo.derecha is None else 0)

    def contarHojas(self):
        return self._contarHojas(self.raiz)

arbol = ArbolBinario()
n = int(input("Ingrese el número de nodos: "))

for i in range(n):
    x = int(input("Ingrese un valor para agregar: "))
    arbol.agregarValor(x)

print(arbol.contarHojas())